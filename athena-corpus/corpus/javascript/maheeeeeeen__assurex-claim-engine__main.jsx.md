# frontend/src/main.jsx

- source repo: maheeeeeeen/assurex-claim-engine
- repo url: https://github.com/maheeeeeeen/assurex-claim-engine
- license: MIT
- created_at: 2026-09-25T19:19:10Z
- file path: frontend/src/main.jsx
- commit: efe52055e383877d0555a86bb366271c74bec50b

```javascript
/**
 * main.jsx — React Entry Point
 *
 * Renders the App component into the DOM root.
 * Imports Bootstrap CSS globally for all components.
 */

import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.jsx';
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```
