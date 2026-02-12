def add(a, b):
    return a - b


if __name__ == "__main__":
    # This runs when we call 'python calc.py'
    result = add(5, 7)
    print(f"Result of 5 + 7 is: {result}")
    assert result == 12, "Calculation Error!"
