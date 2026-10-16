# admin-ui/src/test/java/com/github/klboke/kkrepo/admin/ui/AdminNpmMinimumReleaseAgeContractTest.java

- source repo: klboke/kkRepo
- repo url: https://github.com/klboke/kkRepo
- license: Apache-2.0
- created_at: 2026-06-12
- file path: admin-ui/src/test/java/com/github/klboke/kkrepo/admin/ui/AdminNpmMinimumReleaseAgeContractTest.java
- commit: dd7dc274d1c94a1b92775d410b3dea3f1edf6029

```java
package com.github.klboke.kkrepo.admin.ui;

import static org.junit.jupiter.api.Assertions.assertTrue;

import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.Objects;
import org.junit.jupiter.api.Test;

class AdminNpmMinimumReleaseAgeContractTest {

  @Test
  void npmProxyFormExplainsAndPersistsMinimumReleaseAge() throws IOException {
    String index = resource("/META-INF/resources/admin/index.html");
    String javascript = resource("/META-INF/resources/admin/assets/admin.js");

    assertTrue(index.contains("id=\"repository-minimum-release-age\""));
    assertTrue(index.contains("Use 0 to disable this policy"));
    assertTrue(index.contains("independent of content and metadata cache"));
    assertTrue(index.contains("missing or invalid publish time are blocked"));
    assertTrue(javascript.contains("format === \"npm\" && type === \"PROXY\""));
    assertTrue(javascript.contains("minimumReleaseAgeMinutes: recipe.format === \"npm\""));
    assertTrue(javascript.contains("repo.proxy.minimumReleaseAgeMinutes ?? \"0\""));
  }

  private String resource(String path) throws IOException {
    try (InputStream stream = getClass().getResourceAsStream(path)) {
      return new String(Objects.requireNonNull(stream).readAllBytes(), StandardCharsets.UTF_8);
    }
  }
}
```
