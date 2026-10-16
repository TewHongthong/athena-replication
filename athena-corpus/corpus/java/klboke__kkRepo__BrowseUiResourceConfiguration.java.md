# browse-ui/src/main/java/com/github/klboke/kkrepo/browseui/BrowseUiResourceConfiguration.java

- source repo: klboke/kkRepo
- repo url: https://github.com/klboke/kkRepo
- license: Apache-2.0
- created_at: 2026-06-12
- file path: browse-ui/src/main/java/com/github/klboke/kkrepo/browseui/BrowseUiResourceConfiguration.java
- commit: dd7dc274d1c94a1b92775d410b3dea3f1edf6029

```java
package com.github.klboke.kkrepo.browseui;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class BrowseUiResourceConfiguration implements WebMvcConfigurer {
  @Override
  public void addResourceHandlers(ResourceHandlerRegistry registry) {
    registry
        .addResourceHandler("/browse/**")
        .addResourceLocations("classpath:/META-INF/resources/browse/");
  }
}
```
