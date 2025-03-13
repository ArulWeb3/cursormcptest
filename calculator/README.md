# Calculator API

A FastAPI-based calculator service that provides various mathematical operations through REST API endpoints.

## Features

- Basic arithmetic operations (add, subtract, multiply, divide)
- Advanced operations (power, square root, factorial)
- Input validation
- Error handling
- Swagger documentation

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`
Swagger documentation: `http://localhost:8000/docs`

## API Endpoints

- `POST /add` - Add two numbers
- `POST /subtract` - Subtract second number from first
- `POST /multiply` - Multiply two numbers
- `POST /divide` - Divide first number by second
- `POST /power` - Raise first number to power of second
- `POST /square-root` - Calculate square root
- `POST /factorial` - Calculate factorial

## Example Usage

```bash
# Add two numbers
curl -X POST "http://localhost:8000/add" \
     -H "Content-Type: application/json" \
     -d '{"a": 5, "b": 3}'

# Calculate square root
curl -X POST "http://localhost:8000/square-root" \
     -H "Content-Type: application/json" \
     -d '{"number": 16}'
```