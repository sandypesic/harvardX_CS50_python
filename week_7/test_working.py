import pytest
from week_7.working import convert


def test_digit_format():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_colon_format():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_mixed_format():
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"


def test_overnight_hours():
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"


def test_value_errors():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM - 17:00 PM")