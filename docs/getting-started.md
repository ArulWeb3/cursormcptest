# Getting Started

## Prerequisites

- Odoo 18.0 or later
- Python 3.10+
- PostgreSQL 12+
- Basic understanding of REST APIs

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ArulWeb3/cursormcptest.git
cd cursormcptest
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure Odoo settings:
```bash
cp config/odoo.conf.example config/odoo.conf
# Edit config/odoo.conf with your settings
```

## Basic Usage

1. Start the Odoo server:
```bash
./odoo-bin -c config/odoo.conf
```

2. Access the API endpoints:
```bash
curl http://localhost:8069/api/v1/health
```

## Next Steps

- Review the [Architecture Documentation](./architecture.md)
- Explore the [API Reference](./api-reference.md)
- Set up your [Development Environment](./development-guide.md)