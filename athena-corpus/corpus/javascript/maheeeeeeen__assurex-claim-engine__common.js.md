# frontend/src/api/common.js

- source repo: maheeeeeeen/assurex-claim-engine
- repo url: https://github.com/maheeeeeeen/assurex-claim-engine
- license: MIT
- created_at: 2026-09-25T19:19:10Z
- file path: frontend/src/api/common.js
- commit: efe52055e383877d0555a86bb366271c74bec50b

```javascript
/**
 * Products & Catalog API endpoints
 */

import api from './client';

export const productsAPI = {
  getProducts: (params = {}) => api.get('/api/products/', { params }),
  getProduct: (id) => api.get(`/api/products/${id}`),
  createProduct: (data) => api.post('/api/products/', data),
};

export const warrantiesAPI = {
  getWarranties: (params = {}) => api.get('/api/warranties/', { params }),
  checkWarranty: (productId) => api.get(`/api/warranties/check/${productId}`),
};

export const policiesAPI = {
  getPolicies: () => api.get('/api/policies/'),
  getThresholds: () => api.get('/api/policies/thresholds'),
  updateThresholds: (data) => api.post('/api/policies/thresholds', data),
};

export const adminAPI = {
  getStatus: () => api.get('/api/admin/status'),
  seedDemo: () => api.post('/api/admin/seed'),
  getModelComparison: () => api.get('/api/admin/model-comparison'),
  getAnalytics: () => api.get('/api/admin/analytics'),
};

export default {
  products: productsAPI,
  warranties: warrantiesAPI,
  policies: policiesAPI,
  admin: adminAPI,
};
```
