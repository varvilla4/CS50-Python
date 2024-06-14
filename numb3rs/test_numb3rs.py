from numb3rs import validate

def test_validate():
    assert validate("1.2.3.4") == True
    assert validate("11.22.33.44") == True
    assert validate("123.123.123.123") == True
    assert validate("100.200.300.400") == False
    assert validate("A.B.C.D") == False
    assert validate("?.?.?.?") == False
    

