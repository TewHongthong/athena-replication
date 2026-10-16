# frontend/src/api/claims.js

- source repo: maheeeeeeen/assurex-claim-engine
- repo url: https://github.com/maheeeeeeen/assurex-claim-engine
- license: MIT
- created_at: 2026-09-25T19:19:10Z
- file path: frontend/src/api/claims.js
- commit: efe52055e383877d0555a86bb366271c74bec50b

```javascript
/**
 * Claims API endpoints — submit, list, search, detail, adjudicate, OCR
 */

import api from './client';

export const claimsAPI = {
  // Get paginated/filtered list of claims
  getClaims: (params = {}) => api.get('/api/claims/', { params }),

  // Get executive KPI stats
  getStats: () => api.get('/api/claims/stats/summary'),

  // Get full claim dossier with audit logs and dual-model probabilities
  getClaimDetail: (claimId) => api.get(`/api/claims/${claimId}`),

  // Submit new claim
  submitClaim: (data) => api.post('/api/claims/submit', data),

  // OCR document pre-parse
  processOCR: (formData) =>
    api.post('/api/claims/ocr-process', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    }),

  // Upload evidence media (photo, video, barcode)
  uploadMedia: (formData) =>
    api.post('/api/claims/upload-media', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    }),

  // Real-time cross-document serial & model verification
  crossVerify: (data) => api.post('/api/claims/cross-verify', data),

  // Adjuster decision on a claim
  adjudicateClaim: (claimId, payload) =>
    api.post(`/api/claims/${claimId}/adjudicate`, payload),
};

export default claimsAPI;
```
