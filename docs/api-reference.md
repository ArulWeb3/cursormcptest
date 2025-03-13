# API Reference

## API Versioning

All API endpoints are prefixed with `/api/v1/` for Odoo endpoints and base path `/` for Calculator endpoints.

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

## Calculator API Endpoints

### Basic Operations

#### Add Numbers
```http
POST /add
Content-Type: application/json

{
    "a": 5,
    "b": 3
}

Response:
{
    "result": 8
}
```

#### Subtract Numbers
```http
POST /subtract
Content-Type: application/json

{
    "a": 10,
    "b": 4
}

Response:
{
    "result": 6
}
```

#### Multiply Numbers
```http
POST /multiply
Content-Type: application/json

{
    "a": 6,
    "b": 7
}

Response:
{
    "result": 42
}
```

#### Divide Numbers
```http
POST /divide
Content-Type: application/json

{
    "a": 20,
    "b": 5
}

Response:
{
    "result": 4
}
```

### Advanced Operations

#### Power Operation
```http
POST /power
Content-Type: application/json

{
    "a": 2,
    "b": 3
}

Response:
{
    "result": 8
}
```

#### Square Root
```http
POST /square-root
Content-Type: application/json

{
    "number": 16
}

Response:
{
    "result": 4
}
```

#### Factorial
```http
POST /factorial
Content-Type: application/json

{
    "number": 5
}

Response:
{
    "result": 120
}
```

### Error Responses

```json
{
    "detail": "Error message"
}
```

Common error cases:
- Division by zero
- Negative numbers for square root
- Non-integer or negative numbers for factorial
- Result overflow

## Odoo API Endpoints

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

### Success Response
```json
{
    "result": value,
    "status": "success"
}
```

### Error Response
```json
{
    "detail": "Error description",
    "status": "error"
}
```

## Rate Limiting

API requests are limited to:
- 1000 requests per hour for authenticated users
- 100 requests per hour for unauthenticated users