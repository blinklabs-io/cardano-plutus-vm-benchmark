import org.julclang.core.Program;
import org.julclang.core.flat.UplcFlatDecoder;
import org.julclang.vm.EvalOptions;
import org.julclang.vm.EvalResult;
import org.julclang.vm.PlutusLanguage;
import org.julclang.vm.java.JavaVmProvider;

import java.nio.file.Files;
import java.nio.file.Path;
import java.util.stream.Stream;

/**
 * Evaluates each .flat script once with the arguments CekJavaBenchmark uses and
 * prints "EVAL_FAIL: <script>" for every result that is not a success.
 *
 * CekJavaBenchmark returns the EvalResult without checking it, so JMH times a
 * failed evaluation exactly like a successful one.
 */
public class JulcVerify {
    public static void main(String[] args) throws Exception {
        EvalOptions options = EvalOptions.DEFAULT.withBuiltinTrace(false);
        JavaVmProvider provider = new JavaVmProvider();
        try (Stream<Path> files = Files.list(Path.of(args[0]))) {
            for (Path file : files.filter(p -> p.toString().endsWith(".flat")).sorted().toList()) {
                String name = file.getFileName().toString().replaceFirst("\\.flat$", "");
                try {
                    Program program = UplcFlatDecoder.decodeProgram(Files.readAllBytes(file));
                    EvalResult result = provider.evaluate(program, PlutusLanguage.PLUTUS_V3, null, options);
                    if (!result.isSuccess()) {
                        System.out.println("EVAL_FAIL: " + name + " " + result.getClass().getSimpleName());
                    }
                } catch (Throwable e) {
                    System.out.println("EVAL_FAIL: " + name + " " + e);
                }
            }
        }
    }
}
