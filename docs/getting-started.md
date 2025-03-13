# Getting Started

## Prerequisites

- Python 3.10+
- Docker (optional)
- Git

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

#### For Calculator API
```bash
cd calculator
pip install -r requirements.txt
```

#### For Frontend
```bash
cd calculator-frontend
pip install -r requirements.txt
```

## Running the Applications

### Method 1: Direct Running

1. **Start the Calculator API**
```bash
cd calculator
uvicorn main:app --reload
```
API will be available at `http://localhost:8000`

2. **Start the Frontend**
```bash
cd calculator-frontend
streamlit run app.py
```
Frontend will be available at `http://localhost:8501`

### Method 2: Using Docker

```bash
# Start both services
docker-compose up --build
```

## Quick Start Examples

### Using the Web Interface

1. Open `http://localhost:8501` in your browser
2. Choose between Basic and Advanced operations
3. Enter numbers and select operation
4. Click Calculate to see results

### Using the API Directly

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

## Features

### Basic Operations
- Addition
- Subtraction
- Multiplication
- Division
- Power

### Advanced Operations
- Square Root
- Factorial

## Next Steps

- Review the [Architecture Documentation](./architecture.md)
- Explore the [API Reference](./api-reference.md)
- Check [Deployment Guide](./deployment.md) for production setup