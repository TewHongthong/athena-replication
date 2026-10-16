# frontend/src/api/auth.js

- source repo: maheeeeeeen/assurex-claim-engine
- repo url: https://github.com/maheeeeeeen/assurex-claim-engine
- license: MIT
- created_at: 2026-09-25T19:19:10Z
- file path: frontend/src/api/auth.js
- commit: efe52055e383877d0555a86bb366271c74bec50b

```javascript
/**
 * Auth API endpoints — login, register, profile
 *
 * Wraps all authentication-related HTTP calls.
 * Used by AuthContext to manage user sessions.
 */

import api from './client';

export const authAPI = {
  login: (identifier, password) =>
    api.post('/api/auth/login', { username: identifier, email: identifier, password }),

  register: (userData) =>
    api.post('/api/auth/register', userData),

  getProfile: () =>
    api.get('/api/auth/profile'),

  updateProfile: (data) =>
    api.put('/api/auth/profile', data),
};

export default authAPI;
```
