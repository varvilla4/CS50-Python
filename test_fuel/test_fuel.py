import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/3") == 33
    assert convert("2/3") == 67
    with pytest.raises(ValueError):
        convert ("cat/dog")
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
