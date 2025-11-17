from week_2.plates import is_valid


def test_first_two_letters():
    assert is_valid("HI111") == True
    assert is_valid("111HI") == False


def test_max_char():
    assert is_valid("HELLO") == True
    assert is_valid("HITHERE") == False


def test_min_char():
    assert is_valid("HELLO") == True
    assert is_valid("H") == False


def test_end_numbers():
    assert is_valid("AAA111") == True
    assert is_valid("111AAA") == False
    assert is_valid("A111A") == False


def test_first_number_not_0():
    assert is_valid("AAA100") == True
    assert is_valid("AAA010") == False


def test_no_periods_spaces_punctuation():
    assert is_valid("HELLO") == True
    assert is_valid("HELLO.") == False
    assert is_valid("H E Y") == False
    assert is_valid("HI:)") == False