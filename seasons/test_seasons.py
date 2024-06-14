from seasons import diff_to_words
import pytest

def test_seasons():
    assert diff_to_words("1999-01-01") == "Thirteen million, three hundred fifty-one thousand, six hundred eighty minutes"
    assert diff_to_words("1999-12-31") == "Twelve million, eight hundred twenty-seven thousand, five hundred twenty minutes"
    assert diff_to_words("1970-01-01") == "Twenty-eight million, six hundred four thousand, one hundred sixty minutes"
    with pytest.raises(SystemExit, match="Invalid date"):
        diff_to_words("March 8th, 1999")

