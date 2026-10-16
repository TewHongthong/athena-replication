# admin-ui/src/test/java/com/github/klboke/kkrepo/admin/ui/AdminPypiRemoteIndexPathContractTest.java

- source repo: klboke/kkRepo
- repo url: https://github.com/klboke/kkRepo
- license: Apache-2.0
- created_at: 2026-06-12
- file path: admin-ui/src/test/java/com/github/klboke/kkrepo/admin/ui/AdminPypiRemoteIndexPathContractTest.java
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

class AdminPypiRemoteIndexPathContractTest {

  @Test
  void pypiProxyFormPreservesAnEmptyRemoteIndexPath() throws IOException {
    String index = resource("/META-INF/resources/admin/index.html");
    String javascript = resource("/META-INF/resources/admin/assets/admin.js");

    assertTrue(index.contains("id=\"repository-pypi-index-path\""));
    assertTrue(index.contains("<span class=\"field-label\">Remote Index Path"));
    assertTrue(index.contains("data-tooltip=\"PyPI proxy only."));
    assertTrue(index.contains("Leave this empty"));
    assertTrue(index.contains("Client URLs remain under /simple"));
    assertFalse(index.contains("id=\"repository-pypi-index-path-note\""));
    assertTrue(javascript.contains("format === \"pypi\" && type === \"PROXY\""));
    assertFalse(javascript.contains("repository-pypi-index-path-note"));
    assertTrue(javascript.contains("payload.pypi = {"));
    assertTrue(javascript.contains("repo.pypi?.indexPath ?? \"/simple\""));
    assertTrue(javascript.contains(
        "document.getElementById(\"repository-pypi-index-path\").value = \"/simple\";"));
  }

  private String resource(String path) throws IOException {
    try (InputStream stream = getClass().getResourceAsStream(path)) {
      return new String(Objects.requireNonNull(stream).readAllBytes(), StandardCharsets.UTF_8);
    }
  }
}
```
