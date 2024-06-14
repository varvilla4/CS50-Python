from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"
    assert shorten("CS50") == "CS50"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("APPLE") == "PPL"

if __name__ == "__main__":
    main()

