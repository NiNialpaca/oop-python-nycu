import pytest
import my_recursive as rec

def test_factorial():
    assert rec.factorial(0) == 1
    assert rec.factorial(5) == 120
    assert rec.factorial(3) == 6
    with pytest.raises(ValueError):
        rec.factorial(-1)

def test_fibonacci():
    assert rec.fibonacci(0) == 0
    assert rec.fibonacci(1) == 1
    assert rec.fibonacci(5) == 5
    assert rec.fibonacci(7) == 13
    with pytest.raises(ValueError):
        rec.fibonacci(-3)
