from bank import value

def test_value_zero():
    assert value("HELLO") == 0
    assert value("hello, there") == 0
    assert value("hello") == 0

def test_value_twenty():
    assert value("How are you doing?") == 20
    assert value("How are you?") == 20
    assert value("How was your day?") == 20

def test_value_hundred():
    assert value("Good morning") == 100
    assert value("Great day") == 100

