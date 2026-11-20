// Benchmark harness for the uplc crate of aiken-lang/aiken.
//
// One evaluation is what aiken's own ledger path does (uplc::tx::eval): flat
// decode to FakeNamedDeBruijn, conversion to NamedDeBruijn, then a CEK run as
// Plutus V3 at protocol version 11 (Van Rossem) with the crate's default V3
// cost model for that protocol version and costing on.
//
// In the full tier (the default) each iteration decodes and evaluates. With
// PVB_TIER=eval the program is decoded once before timing; each iteration
// evaluates a clone of it, made in Criterion's untimed setup (the crate's eval
// consumes the program; a clone is cheap because terms hold their children in
// Rc). After warm-up the decoded program is compared with a freshly decoded
// copy, and a script whose evaluation changed it is reported as failed.
//
// A script that does not evaluate successfully is printed as
// "EVAL_FAIL: <name>" and not timed.

use criterion::{BatchSize, Criterion};
use std::{fs, hint::black_box, path::PathBuf};
use uplc::{
    ast::{FakeNamedDeBruijn, NamedDeBruijn, Program},
    machine::{cost_model::ExBudget, eval_result::EvalResult, runtime::VAN_ROSSEM_PROTOCOL_VERSION},
    Language,
};

const DATA_DIR: &str = "/bench/data/plutus_use_cases";

fn scripts() -> Vec<(String, Vec<u8>)> {
    let dir = std::env::var("PVB_DATA_DIR").unwrap_or_else(|_| DATA_DIR.to_string());
    let mut paths: Vec<PathBuf> = fs::read_dir(&dir)
        .unwrap_or_else(|e| panic!("cannot read {dir}: {e}"))
        .map(|entry| entry.unwrap().path())
        .filter(|path| path.is_file() && path.extension().is_some_and(|ext| ext == "flat"))
        .collect();
    paths.sort();
    paths
        .into_iter()
        .map(|path| {
            let name = path.file_stem().unwrap().to_str().unwrap().to_string();
            (name, fs::read(path).unwrap())
        })
        .collect()
}

fn decode(bytes: &[u8]) -> Result<Program<NamedDeBruijn>, String> {
    let program = Program::<FakeNamedDeBruijn>::from_flat(bytes).map_err(|e| e.to_string())?;
    Ok(program.into())
}

fn eval(program: Program<NamedDeBruijn>) -> EvalResult {
    program.eval_version_with_protocol(ExBudget::max(), &Language::PlutusV3, VAN_ROSSEM_PROTOCOL_VERSION)
}

fn decode_and_eval(bytes: &[u8]) -> Result<EvalResult, String> {
    Ok(eval(decode(bytes)?))
}

// A panic inside the crate is returned as an error, so one bad script does not
// stop the run.
fn guarded<R>(f: impl FnOnce() -> R) -> Result<R, String> {
    std::panic::catch_unwind(std::panic::AssertUnwindSafe(f)).map_err(|p| {
        let msg = p
            .downcast_ref::<String>()
            .cloned()
            .or_else(|| p.downcast_ref::<&str>().map(|s| s.to_string()))
            .unwrap_or_default();
        format!("panic: {msg}")
    })
}

fn first_eval(bytes: &[u8]) -> Result<(), String> {
    let result = guarded(|| decode_and_eval(bytes)).and_then(|r| r)?;
    result.result().map(|_| ()).map_err(|e| format!("{e:?}"))
}

fn fail(name: &str, message: &str) {
    let message: String = message.chars().take(200).collect();
    println!("EVAL_FAIL: {name}");
    println!("  {message}");
}

fn bench(c: &mut Criterion) {
    // The default hook prints "panicked", which fill_failures.py would
    // charge to whichever script Criterion printed last.
    std::panic::set_hook(Box::new(|_| {}));
    let eval_tier = std::env::var("PVB_TIER").as_deref() == Ok("eval");

    for (name, bytes) in scripts() {
        if let Err(message) = first_eval(&bytes) {
            fail(&name, &message);
            continue;
        }

        if eval_tier {
            let program = decode(&bytes).expect("decode");
            for _ in 0..3 {
                drop(black_box(eval(program.clone())));
            }
            if program != decode(&bytes).expect("decode") {
                fail(&name, "evaluation modified the decoded program");
                continue;
            }
            println!("PVB_LOOP e3 {name}");
            c.bench_function(&name, |b| {
                b.iter_batched(
                    || program.clone(),
                    |p| drop(black_box(eval(black_box(p)))),
                    BatchSize::SmallInput,
                )
            });
            continue;
        }

        println!("PVB_LOOP d3 {name}");
        c.bench_function(&name, |b| {
            b.iter(|| drop(black_box(decode_and_eval(black_box(&bytes)))))
        });
    }
}

fn main() {
    let mut criterion = Criterion::default().configure_from_args();
    bench(&mut criterion);
    criterion.final_summary();
}
