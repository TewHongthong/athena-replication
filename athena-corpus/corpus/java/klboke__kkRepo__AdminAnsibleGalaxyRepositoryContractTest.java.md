# admin-ui/src/test/java/com/github/klboke/kkrepo/admin/ui/AdminAnsibleGalaxyRepositoryContractTest.java

- source repo: klboke/kkRepo
- repo url: https://github.com/klboke/kkRepo
- license: Apache-2.0
- created_at: 2026-06-12
- file path: admin-ui/src/test/java/com/github/klboke/kkrepo/admin/ui/AdminAnsibleGalaxyRepositoryContractTest.java
- commit: dd7dc274d1c94a1b92775d410b3dea3f1edf6029

```java
package com.github.klboke.kkrepo.admin.ui;

import static org.junit.jupiter.api.Assertions.assertTrue;

import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.Objects;
import org.junit.jupiter.api.Test;

class AdminAnsibleGalaxyRepositoryContractTest {

  @Test
  void configuresDefaultRemoteAndNestedGroups() throws IOException {
    String javascript = resource("/META-INF/resources/admin/assets/admin.js");

    assertTrue(javascript.contains("ansiblegalaxy: \"Ansible Galaxy\""));
    assertTrue(javascript.contains("ansiblegalaxy: \"https://galaxy.ansible.com/\""));
    assertTrue(javascript.contains("format === \"ansiblegalaxy\""));
  }

  private String resource(String path) throws IOException {
    try (InputStream stream = getClass().getResourceAsStream(path)) {
      return new String(Objects.requireNonNull(stream).readAllBytes(), StandardCharsets.UTF_8);
    }
  }
}
```
