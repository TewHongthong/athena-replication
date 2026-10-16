# admin-ui/src/test/java/com/github/klboke/kkrepo/admin/ui/AdminSessionHydrationContractTest.java

- source repo: klboke/kkRepo
- repo url: https://github.com/klboke/kkRepo
- license: Apache-2.0
- created_at: 2026-06-12
- file path: admin-ui/src/test/java/com/github/klboke/kkrepo/admin/ui/AdminSessionHydrationContractTest.java
- commit: dd7dc274d1c94a1b92775d410b3dea3f1edf6029

```java
package com.github.klboke.kkrepo.admin.ui;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.Objects;
import org.junit.jupiter.api.Test;

class AdminSessionHydrationContractTest {

  @Test
  void administrationHydratesCachedUserBeforeSessionProbeCompletes() throws IOException {
    String javascript = resource("/META-INF/resources/admin/assets/admin.js");

    assertTrue(javascript.contains("function hydrateSessionControls()"));
    assertTrue(javascript.contains("hydrateSessionControls();\nloadCurrentSession({ quiet: true })"));
  }

  @Test
  void passwordLoginRefreshesTheCurrentPageWithoutAFullReload() throws IOException {
    String login = resource("/META-INF/resources/login/assets/login-modal.js");

    assertTrue(login.contains("new CustomEvent(\"kkrepo:login-success\""));
    assertFalse(login.contains("window.location.reload()"));
  }

  private String resource(String path) throws IOException {
    try (InputStream stream = getClass().getResourceAsStream(path)) {
      return new String(Objects.requireNonNull(stream).readAllBytes(), StandardCharsets.UTF_8);
    }
  }
}
```
