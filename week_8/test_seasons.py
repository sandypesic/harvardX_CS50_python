import pytest
from datetime import date
import builtins
from seasons import convert, calc_minutes, get_date


def test_convert_basic():
    assert convert(525600) == "five hundred twenty-five thousand, six hundred"


def test_convert_large():
    assert convert(1051200) == "one million, fifty-one thousand, two hundred"


def test_convert_negative():
    assert convert(-525600) == "minus five hundred twenty-five thousand, six hundred"


def test_calc_minutes_basic():
    birthday = date.today().replace(year=date.today().year - 1)
    expected = 365 * 24 * 60
    assert calc_minutes(birthday) == expected


def test_calc_minutes_future():
    future = date.today().replace(year=date.today().year + 1)
    expected = -365 * 24 * 60
    assert calc_minutes(future) == expected


def test_get_date_valid(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda _: "2025-01-01")
    assert get_date() == date(2025, 1, 1)


def test_get_date_invalid(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda _: "not-a-date")
    with pytest.raises(SystemExit):
        get_date()


def test_get_date_invalid_format(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda _: "2025/01/01")
    with pytest.raises(SystemExit):
        get_date()