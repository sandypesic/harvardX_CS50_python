from week_2.twttr import shorten

def test_argument():
    assert shorten("Sandy") == "Sndy"
    assert shorten("HELLO") == "HLL"

def test_no_vowels():
    assert shorten("rhythm") == "rhythm"

def test_all_vowels():
    assert shorten("aeiouAEIOU") == ""

def test_empty():
    assert shorten("") == ""

def test_numbers_and_punctuation():
    assert shorten("H3ll0, W0rld!") == "H3ll0, W0rld!"