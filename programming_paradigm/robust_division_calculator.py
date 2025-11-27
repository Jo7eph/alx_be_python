def safe_divide(numerator, denominator):
    """
    Safely divide two numbers, handling division by zero and non-numeric inputs.

    Parameters:
        numerator: The numerator value (can be string or number)
        denominator: The denominator value (can be string or number)

    Returns:
        str: Result of division or error message
    """
    try:
        # Convert inputs to float
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / denom
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result}"
