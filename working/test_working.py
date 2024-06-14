from working import convert
import pytest

def test1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("11 PM to 11 AM") == "23:00 to 11:00"
    assert convert("7:15 PM to 3:00 AM") == "19:15 to 03:00"

def test2():
    with pytest.raises(ValueError):
        convert("1:65 AM to 1:65 PM")
    with pytest.raises(ValueError):
        convert("12:80 AM to 8:90 AM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
