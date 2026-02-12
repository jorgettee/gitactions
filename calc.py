def add(a, b):
    return a + b
if __name__ == "__main__":
    result = add(5, 7)
    print(f"Checking 5 + 7... Result: {result}")
    # A simple assertion to make the script fail if the math is wrong
    assert result == 12, "Math error: 5 + 7 should be 12"
    print("Test passed!")
