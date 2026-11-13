// Benchmark harness for the released amaru-uplc crate.
//
// In the full tier (the default), each iteration decodes one flat-encoded
// Plutus V3 program and evaluates it at protocol version 11 with the crate's
// default V3 cost model. With PVB_TIER=eval, the program is decoded once
// before timing and each iteration only evaluates it.

use amaru_kernel::{PlutusVersion, protocol_version::PROTOCOL_VERSION_11};
use amaru_uplc::{
    arena::Arena,
    binder::DeBruijn,
    flat,
    machine::{CostModel, ExBudget},
};
use bumpalo::Bump;
use criterion::Criterion;
use std::{fs, path::PathBuf};

const DATA_DIR: &str = "benches/use_cases/plutus_use_cases";

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

fn eval_once(arena: &Arena, bytes: &[u8], cost_model: &CostModel) -> Result<(), String> {
    let (program, _) =
        flat::decode::<DeBruijn>(arena, bytes, PlutusVersion::V3, PROTOCOL_VERSION_11)
            .map_err(|e| format!("decode: {e:?}"))?;
    let result = program.eval(arena, cost_model.clone(), ExBudget::max());
    if result.is_success() {
        Ok(())
    } else {
        Err(format!("{:?}", result.error()))
    }
}

fn bench(c: &mut Criterion) {
    let eval_tier = std::env::var("PVB_TIER").as_deref() == Ok("eval");
    let cost_model = CostModel::v3();
    let mut arena = Arena::from_bump(Bump::with_capacity(10_485_760));

    for (name, bytes) in scripts() {
        let first = eval_once(&arena, &bytes, &cost_model);
        arena.reset();
        if let Err(message) = first {
            let message: String = message.chars().take(200).collect();
            println!("EVAL_FAIL: {name}");
            println!("  {message}");
            continue;
        }

        if eval_tier {
            println!("PVB_LOOP e3 {name}");
            let decode_arena = Arena::from_bump(Bump::with_capacity(10_485_760));
            let (program, _) = flat::decode::<DeBruijn>(
                &decode_arena,
                &bytes,
                PlutusVersion::V3,
                PROTOCOL_VERSION_11,
            )
            .expect("decode");
            let mut eval_arena = Arena::from_bump(Bump::with_capacity(10_485_760));
            c.bench_function(&name, |b| {
                b.iter(|| {
                    let result = program.eval(&eval_arena, cost_model.clone(), ExBudget::max());
                    std::hint::black_box(result.is_success());
                    drop(result);
                    eval_arena.reset();
                })
            });
            continue;
        }

        println!("PVB_LOOP d3 {name}");
        let mut decode_arena = Arena::from_bump(Bump::with_capacity(10_485_760));
        let mut eval_arena = Arena::from_bump(Bump::with_capacity(10_485_760));
        c.bench_function(&name, |b| {
            b.iter(|| {
                let (program, _) = flat::decode::<DeBruijn>(
                    &decode_arena,
                    &bytes,
                    PlutusVersion::V3,
                    PROTOCOL_VERSION_11,
                )
                .expect("decode");
                let result = program.eval(&eval_arena, cost_model.clone(), ExBudget::max());
                std::hint::black_box(result.is_success());
                drop(result);
                decode_arena.reset();
                eval_arena.reset();
            })
        });
    }
}

fn main() {
    let mut criterion = Criterion::default().configure_from_args();
    bench(&mut criterion);
    criterion.final_summary();
}
