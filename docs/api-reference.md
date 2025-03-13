# API Reference

## API Versioning

All API endpoints are prefixed with `/api/v1/` to ensure proper versioning.

## Authentication

```http
POST /api/v1/auth/token
Content-Type: application/json

{
    "db": "odoo_db",
    "login": "user@example.com",
    "password": "secure_password"
}
```

## Common Endpoints

### Health Check

```http
GET /api/v1/health
```

### Partners

```http
GET /api/v1/partners
GET /api/v1/partners/{id}
POST /api/v1/partners
PUT /api/v1/partners/{id}
DELETE /api/v1/partners/{id}
```

### Products

```http
GET /api/v1/products
GET /api/v1/products/{id}
POST /api/v1/products
PUT /api/v1/products/{id}
DELETE /api/v1/products/{id}
```

## Response Format

```json
{
    "status": "success",
    "data": {},
    "message": ""
}
```

## Error Handling

```json
{
    "status": "error",
    "code": "ERROR_CODE",
    "message": "Error description"
}
```

## Rate Limiting

API requests are limited to:
- 1000 requests per hour for authenticated users
- 100 requests per hour for unauthenticated users