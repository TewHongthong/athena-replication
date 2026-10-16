# browse-ui/src/main/java/com/github/klboke/kkrepo/browseui/BrowseUiController.java

- source repo: klboke/kkRepo
- repo url: https://github.com/klboke/kkRepo
- license: Apache-2.0
- created_at: 2026-06-12
- file path: browse-ui/src/main/java/com/github/klboke/kkrepo/browseui/BrowseUiController.java
- commit: dd7dc274d1c94a1b92775d410b3dea3f1edf6029

```java
package com.github.klboke.kkrepo.browseui;

import org.springframework.core.io.ClassPathResource;
import org.springframework.core.io.Resource;
import org.springframework.http.CacheControl;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class BrowseUiController {
  private static final Resource BROWSE_INDEX =
      new ClassPathResource("META-INF/resources/browse/index.html");

  @GetMapping({"/browse", "/browse/", "/browse/index.html"})
  public ResponseEntity<Resource> browse() {
    return ResponseEntity.ok()
        .contentType(MediaType.TEXT_HTML)
        .cacheControl(CacheControl.noCache())
        .body(BROWSE_INDEX);
  }
}
```
