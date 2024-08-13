# CLI Calc v1

import re

def evaluate_expression(expression):
    try:
        # Evaluate the sanitized expression
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"

def sanitize_expression(expression):
    # Use regex to remove any characters that are not digits, operators, or parentheses
    sanitized = re.sub(r'[^0-9+\-*/().]', '', expression)
    return sanitized

def main():
    # Input
    expression = input("Enter a mathematical expression: ")
    
    # Sanitize the input to ensure it only contains valid characters
    sanitized_expression = sanitize_expression(expression)
    
    # Evaluate the sanitized expression
    result = evaluate_expression(sanitized_expression)
    
    # Output
    print(f"The result is: {result}")
    input()

if __name__ == "__main__":
    main()
