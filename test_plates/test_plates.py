from plates import is_valid

def test_length():
    assert is_valid("CS50") == True
    assert is_valid("C") == False

def test_start_with_letters():
    assert is_valid("AB134") == True
    assert is_valid("1234") == False

def test_characters():
    assert is_valid("AB#34") == False
    assert is_valid("!@#$") == False

def test_letter_after_number():
    assert is_valid("ABC3F") == False
    assert is_valid("23ABC") == False

def test_no_zero_first():
    assert is_valid("ABC01") == False
    assert is_valid("ABC10") == True
    
