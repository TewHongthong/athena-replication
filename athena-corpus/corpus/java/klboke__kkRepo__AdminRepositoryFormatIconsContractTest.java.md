# admin-ui/src/test/java/com/github/klboke/kkrepo/admin/ui/AdminRepositoryFormatIconsContractTest.java

- source repo: klboke/kkRepo
- repo url: https://github.com/klboke/kkRepo
- license: Apache-2.0
- created_at: 2026-06-12
- file path: admin-ui/src/test/java/com/github/klboke/kkrepo/admin/ui/AdminRepositoryFormatIconsContractTest.java
- commit: dd7dc274d1c94a1b92775d410b3dea3f1edf6029

```java
package com.github.klboke.kkrepo.admin.ui;

import static org.junit.jupiter.api.Assertions.assertTrue;

import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.List;
import java.util.Objects;
import org.junit.jupiter.api.Test;

class AdminRepositoryFormatIconsContractTest {
  private static final List<String> FORMATS = List.of(
      "maven2", "npm", "pypi", "cargo", "pub", "composer", "terraform", "swift",
      "ansiblegalaxy", "conda", "conan", "apt", "alpine", "huggingface", "go",
      "helm", "docker", "nuget", "rubygems", "yum", "raw");

  @Test
  void repositoryFormatColumnUsesSharedBrandIcons() throws IOException {
    String index = resource("/META-INF/resources/admin/index.html");
    String javascript = resource("/META-INF/resources/admin/assets/admin.js");

    assertTrue(index.contains("/browse/assets/format-icons.css"));
    assertTrue(javascript.contains("<td>${formatBadge(repo.format)}</td>"));
    for (String format : FORMATS) {
      assertTrue(javascript.contains(format + ": \"" + iconName(format) + "\""), format);
    }
  }

  private static String iconName(String format) {
    return "maven2".equals(format) ? "maven" : format;
  }

  private String resource(String path) throws IOException {
    try (InputStream stream = getClass().getResourceAsStream(path)) {
      return new String(Objects.requireNonNull(stream).readAllBytes(), StandardCharsets.UTF_8);
    }
  }
}
```
