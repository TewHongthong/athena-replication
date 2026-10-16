# admin-ui/src/main/java/com/github/klboke/kkrepo/adminui/AdminUiResourceConfiguration.java

- source repo: klboke/kkRepo
- repo url: https://github.com/klboke/kkRepo
- license: Apache-2.0
- created_at: 2026-06-12
- file path: admin-ui/src/main/java/com/github/klboke/kkrepo/adminui/AdminUiResourceConfiguration.java
- commit: dd7dc274d1c94a1b92775d410b3dea3f1edf6029

```java
package com.github.klboke.kkrepo.adminui;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class AdminUiResourceConfiguration implements WebMvcConfigurer {
  @Override
  public void addResourceHandlers(ResourceHandlerRegistry registry) {
    registry
        .addResourceHandler("/admin/**")
        .addResourceLocations("classpath:/META-INF/resources/admin/");
    registry
        .addResourceHandler("/login/**")
        .addResourceLocations("classpath:/META-INF/resources/login/");
  }
}
```
