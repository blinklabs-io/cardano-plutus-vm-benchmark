// Benchmark: flat-decode + CEK evaluate, over the plutus_use_cases corpus.
//
// Written for cardano-plutus-vm-benchmark, which runs each VM's own benchmark
// rather than a shared harness. It reads the canonical .flat scripts from
// bench/plutus_use_cases (the benchmark repo symlinks them there) and writes
// bench/results/plutus_use_cases.json.
//
//   node bench/bench.mjs
//
// Warmup 5 iterations, then at least 50 iterations and at least 5 seconds per
// script, matching the other custom runners in that suite.
//
// PVB_TIER=eval decodes each script once before timing and times evaluation
// only, writing bench/results/plutus_use_cases-eval.json. It checks that
// evaluation leaves the decoded program unchanged, so that every timed
// iteration evaluates the same program.

import { readFileSync, readdirSync, mkdirSync, writeFileSync, existsSync } from "fs";
import { dirname, join } from "path";
import { fileURLToPath } from "url";
import { createRequire } from "module";

// plutus-machine reads process.env.PEBBLE_PROFILE on every CEK step. That is a
// native lookup in Node, so a plain copy keeps it out of the measured time.
process.env = { ...process.env };

const require = createRequire(import.meta.url);
const { UPLCDecoder, showUPLC } = require("@harmoniclabs/uplc");
const { CEKError, Machine } = require("../dist/index.js");

const HERE = dirname(fileURLToPath(import.meta.url));
const DATA_DIR = process.env.BENCH_DATA ?? join(HERE, "plutus_use_cases");
const OUT_DIR = join(HERE, "results");
const EVAL_TIER = process.env.PVB_TIER === "eval";
const OUT_FILE = join(OUT_DIR, EVAL_TIER ? "plutus_use_cases-eval.json" : "plutus_use_cases.json");

const WARMUP = Number(process.env.BENCH_WARMUP ?? 5);
const MIN_ITERATIONS = Number(process.env.BENCH_MIN_ITERS ?? 50);
const TIME_BUDGET_NS = Number(process.env.BENCH_BUDGET_NS ?? 5e9);

if (!existsSync(DATA_DIR)) {
  console.error(`no benchmark data at ${DATA_DIR}`);
  process.exit(1);
}

/** evaluate a decoded program body. */
function evaluate(body) {
  const result = Machine.evalSimple(body);
  if (result instanceof CEKError) {
    throw new Error(result.msg ?? "CEK evaluation failed");
  }
  return result;
}

/** flat-decode then evaluate, which the full tier measures. */
function runScript(bytes) {
  return evaluate(UPLCDecoder.parse(bytes, "flat").body);
}

function summarise(samples) {
  const sorted = [...samples].sort((a, b) => a - b);
  const mean = sorted.reduce((a, b) => a + b, 0) / sorted.length;
  const variance = sorted.reduce((a, b) => a + (b - mean) ** 2, 0) / sorted.length;
  return {
    mean_ns: Math.round(mean),
    median_ns: sorted.length % 2
      ? sorted[sorted.length >> 1]
      : Math.round((sorted[sorted.length / 2 - 1] + sorted[sorted.length / 2]) / 2),
    min_ns: sorted[0],
    max_ns: sorted[sorted.length - 1],
    stddev_ns: Math.round(Math.sqrt(variance)),
    iterations: sorted.length,
  };
}

const files = readdirSync(DATA_DIR).filter((f) => f.endsWith(".flat")).sort();
const benchmarks = [];
let failed = 0;

for (const file of files) {
  const name = file.replace(/\.flat$/, "");
  const bytes = new Uint8Array(readFileSync(join(DATA_DIR, file)));
  // The eval tier decodes once, before timing, and evaluates that program.
  let run = () => runScript(bytes);

  try {
    if (EVAL_TIER) {
      const body = UPLCDecoder.parse(bytes, "flat").body;
      const decoded = showUPLC(body);
      run = () => evaluate(body);
      for (let i = 0; i < WARMUP; i++) run();
      if (showUPLC(body) !== decoded) {
        throw new Error("evaluation modified the decoded program");
      }
    } else {
      for (let i = 0; i < WARMUP; i++) run();
    }
  } catch (err) {
    console.error(`${name}: ${String(err).split("\n")[0]}`);
    failed++;
    continue;
  }

  const samples = [];
  const started = process.hrtime.bigint();
  while (
    samples.length < MIN_ITERATIONS ||
    Number(process.hrtime.bigint() - started) < TIME_BUDGET_NS
  ) {
    const t0 = process.hrtime.bigint();
    run();
    samples.push(Number(process.hrtime.bigint() - t0));
  }

  const stats = summarise(samples);
  benchmarks.push({ name, ...stats });
  console.log(`${name.padEnd(28)} ${(stats.mean_ns / 1e6).toFixed(3)} ms  (n=${stats.iterations})`);
}

mkdirSync(OUT_DIR, { recursive: true });
writeFileSync(OUT_FILE, JSON.stringify({ benchmarks }, null, 2));

const ok = benchmarks.length;
const geomean = ok
  ? Math.exp(benchmarks.reduce((a, b) => a + Math.log(b.mean_ns), 0) / ok)
  : 0;
console.log(`\n${ok} scripts, ${failed} failed, geometric mean ${(geomean / 1e6).toFixed(3)} ms`);
console.log(`wrote ${OUT_FILE}`);
