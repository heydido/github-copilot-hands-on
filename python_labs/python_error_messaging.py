### Initial Code:
def divide_numbers(numerator, divisor):
    """Divide two numbers and handle division by zero."""
    try:
        return numerator / divisor
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

def main():
    result = divide_numbers(10, 0)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()