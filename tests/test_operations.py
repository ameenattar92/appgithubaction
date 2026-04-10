from src.math_operations import add, sub # Modular coding way to import functions from src

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0

def test_sub():
    assert sub(5,2) == 3
    assert sub(0,1) == -1
    assert sub(10,5) == 5
    assert sub(-1,-1) == 0

    