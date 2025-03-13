# Calculator Frontend

A Streamlit-based frontend for the Calculator API. This application provides a user-friendly interface for performing various mathematical operations.

## Features

- Basic arithmetic operations (add, subtract, multiply, divide)
- Advanced operations (power, square root, factorial)
- User-friendly interface
- Real-time calculations
- Error handling and display

## Prerequisites

- Python 3.10+
- Calculator API running locally

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
streamlit run app.py
```

## Usage

1. The application will open in your default web browser
2. Select the operation type (Basic or Advanced)
3. Enter the required numbers
4. Click Calculate to see the result

## API Connection

The frontend assumes the Calculator API is running at `http://localhost:8000`. If your API is running on a different address, update the `API_BASE_URL` in `app.py`.