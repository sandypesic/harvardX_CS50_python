import pytest
from week_3.fuel import convert, gauge


def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("0/1") == 0
    assert convert("100/100") == 100


def test_convert_invalid_valueerror():
    with pytest.raises(ValueError):
        convert("5/3")
    with pytest.raises(ValueError):
        convert("3/a")
        convert("b/4")


def test_convert_invalid_zerodivision():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")


def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_percentage():
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"