# utils.py - A simple utility module

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b

def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b

def divide(a, b):
    """Divide a by b and return the result. Raises an error if b is zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed!")
    return a / b

def greet(name):
    """Return a personalized greeting message."""
    return f"Hello, {name}! How can I assist you today?"