# Getting Started

## Prerequisites

- Odoo 18.0 or later
- Python 3.10+
- PostgreSQL 12+
- Basic understanding of REST APIs

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/ArulWeb3/cursormcptest.git
cd cursormcptest
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

### 3. Install Dependencies
```bash
# For Calculator API
cd calculator
pip install -r requirements.txt

# For Odoo API
cd ../odoo
pip install -r requirements.txt
```

### 4. Configure Settings
```bash
# For Odoo
cp config/odoo.conf.example config/odoo.conf
# Edit config/odoo.conf with your settings
```

## Running the Services

### Calculator API
```bash
cd calculator
uvicorn main:app --reload
# API will be available at http://localhost:8000
# Swagger docs at http://localhost:8000/docs
```

### Odoo Server
```bash
cd odoo
./odoo-bin -c config/odoo.conf
```

## Quick Start Examples

### Calculator API

1. Add two numbers:
```bash
curl -X POST "http://localhost:8000/add" \
     -H "Content-Type: application/json" \
     -d '{"a": 5, "b": 3}'
```

2. Calculate square root:
```bash
curl -X POST "http://localhost:8000/square-root" \
     -H "Content-Type: application/json" \
     -d '{"number": 16}'
```

### Odoo API

1. Get authentication token:
```bash
curl -X POST "http://localhost:8069/api/v1/auth/token" \
     -H "Content-Type: application/json" \
     -d '{"db":"odoo_db","login":"user@example.com","password":"pass"}'
```

2. List partners:
```bash
curl "http://localhost:8069/api/v1/partners" \
     -H "Authorization: Bearer YOUR_TOKEN"
```

## Next Steps

- Review the [Architecture Documentation](./architecture.md)
- Explore the [API Reference](./api-reference.md)
- Set up your [Development Environment](./development-guide.md)