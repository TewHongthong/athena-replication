# admin-ui/src/test/java/com/github/klboke/kkrepo/admin/ui/AdminGlobalComponentSearchContractTest.java

- source repo: klboke/kkRepo
- repo url: https://github.com/klboke/kkRepo
- license: Apache-2.0
- created_at: 2026-06-12
- file path: admin-ui/src/test/java/com/github/klboke/kkrepo/admin/ui/AdminGlobalComponentSearchContractTest.java
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

class AdminGlobalComponentSearchContractTest {

  @Test
  void administrationExposesTheSharedGlobalSearch() throws IOException {
    String index = resource("/META-INF/resources/admin/index.html");
    String translations = resource("/META-INF/resources/login/assets/ui-i18n.js");

    assertTrue(index.contains("data-global-component-search action=\"/browse/\""));
    assertTrue(index.indexOf("class=\"top-spacer\"")
        < index.indexOf("<form class=\"global-component-search\""));
    assertTrue(index.contains("placeholder=\"Search components\""));
    assertFalse(index.contains("<button type=\"submit\">Search</button>"));
    assertTrue(index.contains(
        "/browse/assets/global-component-search.css?v=20260819-topbar-control-height-1"));
    assertTrue(index.contains("/browse/assets/global-component-search.js"));
    assertTrue(translations.contains("\"Search components\": \"搜索组件\""));
    assertTrue(translations.contains("\"All formats\": \"全部格式\""));
  }

  private String resource(String path) throws IOException {
    try (InputStream stream = getClass().getResourceAsStream(path)) {
      return new String(Objects.requireNonNull(stream).readAllBytes(), StandardCharsets.UTF_8);
    }
  }
}
```
