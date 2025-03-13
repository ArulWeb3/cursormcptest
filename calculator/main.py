from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import math

app = FastAPI(
    title="Calculator API",
    description="A REST API for performing calculator operations",
    version="1.0.0"
)

class CalculationRequest(BaseModel):
    a: float
    b: float

class AdvancedCalculationRequest(BaseModel):
    number: float
    power: Optional[float] = None

@app.get("/")
async def root():
    return {"message": "Welcome to Calculator API"}

@app.post("/add")
async def add(req: CalculationRequest):
    """Add two numbers"""
    return {"result": req.a + req.b}

@app.post("/subtract")
async def subtract(req: CalculationRequest):
    """Subtract second number from first number"""
    return {"result": req.a - req.b}

@app.post("/multiply")
async def multiply(req: CalculationRequest):
    """Multiply two numbers"""
    return {"result": req.a * req.b}

@app.post("/divide")
async def divide(req: CalculationRequest):
    """Divide first number by second number"""
    if req.b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": req.a / req.b}

@app.post("/power")
async def power(req: CalculationRequest):
    """Raise first number to the power of second number"""
    try:
        return {"result": math.pow(req.a, req.b)}
    except OverflowError:
        raise HTTPException(status_code=400, detail="Result too large")

@app.post("/square-root")
async def square_root(req: AdvancedCalculationRequest):
    """Calculate square root of a number"""
    if req.number < 0:
        raise HTTPException(status_code=400, detail="Cannot calculate square root of negative number")
    return {"result": math.sqrt(req.number)}

@app.post("/factorial")
async def factorial(req: AdvancedCalculationRequest):
    """Calculate factorial of a number"""
    if req.number < 0 or not req.number.is_integer():
        raise HTTPException(status_code=400, detail="Number must be a positive integer")
    try:
        return {"result": math.factorial(int(req.number))}
    except OverflowError:
        raise HTTPException(status_code=400, detail="Result too large")