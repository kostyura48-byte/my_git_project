from app import add

def test_positive():
    assert add(2, 3) == 5

def test_zero():
    assert add(0, 5) == 5

def test_negative():
    assert add(-1, -1) == -2
