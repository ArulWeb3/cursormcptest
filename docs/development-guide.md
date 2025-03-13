# Development Guide

## Development Environment Setup

### Required Tools

- Python 3.10+
- PostgreSQL 12+
- Git
- Visual Studio Code (recommended)

### Project Structure

```
project_root/
├── calculator/          # Calculator API service
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
├── odoo/               # Odoo API service
│   ├── addons/
│   ├── config/
│   └── requirements.txt
├── docs/               # Documentation
└── tests/              # Test suites
```

## Development Workflow

1. **Branch Management**
   - `main`: Production-ready code
   - `dev`: Development branch
   - Feature branches: `feature/feature-name`

2. **Code Style**
   - Follow PEP 8
   - Use meaningful variable names
   - Add docstrings

3. **Testing**

   Calculator API:
   ```bash
   cd calculator
   pytest
   ```

   Odoo API:
   ```bash
   cd odoo
   python -m pytest
   ```

## API Development Guidelines

### Calculator API

1. **Adding New Endpoints**
   ```python
   @app.post("/new-operation")
   async def new_operation(req: CalculationRequest):
       # Input validation
       # Operation logic
       # Return result
   ```

2. **Error Handling**
   ```python
   if invalid_condition:
       raise HTTPException(
           status_code=400,
           detail="Error message"
       )
   ```

### Odoo API

1. **Model Creation**
   ```python
   class NewModel(models.Model):
       _name = 'new.model'
       _description = 'New Model'
   ```

2. **Controller Development**
   ```python
   @http.route('/api/v1/new-endpoint', auth='user')
   def new_endpoint(self):
       # Implementation
   ```

## Testing Guidelines

1. **Unit Tests**
   ```python
   def test_addition():
       response = client.post(
           "/add",
           json={"a": 2, "b": 3}
       )
       assert response.status_code == 200
       assert response.json()["result"] == 5
   ```

2. **Integration Tests**
   ```python
   def test_workflow():
       # Test complete workflow
       pass
   ```

## Documentation

1. **Code Documentation**
   ```python
   def function_name(param: type) -> return_type:
       """Function description.

       Args:
           param: Parameter description

       Returns:
           Return value description

       Raises:
           Exception: Error condition
       """
   ```

2. **API Documentation**
   - Update Swagger docs
   - Update README.md
   - Update API reference

## Deployment

1. **Local Development**
   ```bash
   uvicorn main:app --reload
   ```

2. **Production**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

## Best Practices

1. **Code Quality**
   - Write clean, readable code
   - Follow DRY principles
   - Add proper comments

2. **Security**
   - Validate all inputs
   - Handle errors gracefully
   - Follow security best practices

3. **Performance**
   - Optimize database queries
   - Use appropriate data structures
   - Consider caching when needed