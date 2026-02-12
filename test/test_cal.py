from calc import add

def test_addition_simple():
    # Test simple positive numbers
    assert add(5, 7) == 12

def test_addition_negative():
    # Test if it handles negative numbers correctly
    assert add(-1, 1) == 0
    assert add(-5, -5) == -10

def test_addition_zero():
    # Test adding zero
    assert add(10, 0) == 10
