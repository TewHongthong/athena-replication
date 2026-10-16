# admin-ui/src/test/java/com/github/klboke/kkrepo/admin/ui/AdminToastLayerContractTest.java

- source repo: klboke/kkRepo
- repo url: https://github.com/klboke/kkRepo
- license: Apache-2.0
- created_at: 2026-06-12
- file path: admin-ui/src/test/java/com/github/klboke/kkrepo/admin/ui/AdminToastLayerContractTest.java
- commit: dd7dc274d1c94a1b92775d410b3dea3f1edf6029

```java
package com.github.klboke.kkrepo.admin.ui;

import static org.junit.jupiter.api.Assertions.assertTrue;

import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.Objects;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import org.junit.jupiter.api.Test;

class AdminToastLayerContractTest {
  private static final Pattern Z_INDEX = Pattern.compile("z-index:\\s*(\\d+)");

  @Test
  void errorToastsRenderAboveRepositoryFormModal() throws IOException {
    String stylesheet = resource("/META-INF/resources/admin/assets/admin.css");

    assertTrue(zIndex(stylesheet, ".toast-region") > zIndex(stylesheet, ".form-modal"),
        "repository save errors must remain visible while the form modal is open");
  }

  private int zIndex(String stylesheet, String selector) {
    int selectorStart = stylesheet.indexOf(selector + " {");
    int blockEnd = stylesheet.indexOf('}', selectorStart);
    assertTrue(selectorStart >= 0 && blockEnd > selectorStart,
        "missing CSS block for " + selector);
    Matcher matcher = Z_INDEX.matcher(stylesheet.substring(selectorStart, blockEnd));
    assertTrue(matcher.find(), "missing z-index for " + selector);
    return Integer.parseInt(matcher.group(1));
  }

  private String resource(String path) throws IOException {
    try (InputStream stream = getClass().getResourceAsStream(path)) {
      return new String(Objects.requireNonNull(stream).readAllBytes(), StandardCharsets.UTF_8);
    }
  }
}
```
