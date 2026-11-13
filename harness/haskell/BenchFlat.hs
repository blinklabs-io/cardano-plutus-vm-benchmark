{-# LANGUAGE BangPatterns #-}

{-| The full tier of cardano-plutus-vm-benchmark for plutus-core: each
iteration decodes a whole data/*.flat file, Data arguments included, and
evaluates it like the validation benchmark (BenchCek.hs) does.

The validation benchmark decodes before timing, so it is the eval tier.
validation-full (BenchFull.hs) peels the Data arguments off before timing,
so it never decodes them in the loop. This benchmark decodes and fully
forces the whole program in the timed loop, which is what the other VMs'
full tier times. -}
module Main where

import Control.DeepSeq (force)
import Control.Exception (evaluate)
import Criterion (whnf)
import PlutusBenchmark.Common (evaluateCekLikeInProd, toNamedDeBruijnTerm)
import PlutusBenchmark.Validation.Common (benchWith, mkEvalCtx, unsafeUnflat)
import PlutusCore.Default (BuiltinSemanticsVariant (DefaultFunSemanticsVariantE))
import PlutusLedgerApi.Common (PlutusLedgerLanguage (PlutusV3))
import UntypedPlutusCore qualified as UPLC

main :: IO ()
main = do
  -- The same evaluation context as the validation benchmark.
  evalCtx <- evaluate $ mkEvalCtx PlutusV3 DefaultFunSemanticsVariantE
  let decodeAndEval file bytes =
        let !term = force . toNamedDeBruijnTerm . UPLC._progTerm $ unsafeUnflat file bytes
         in either (error . show) (const ()) (evaluateCekLikeInProd evalCtx term)
  benchWith $ \file bytes -> whnf (decodeAndEval file) bytes
