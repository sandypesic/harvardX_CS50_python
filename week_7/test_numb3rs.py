import pytest
from week_7.numb3rs import validate


def test_valid_ip():
    assert validate("127.0.0.1") == True


def test_range_exceeded():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False


def test_preceding_zeroes():
    assert validate("192.168.001.1") == False


def test_numbers_only():
    assert validate("cat") == False


def test_boundary_numbers():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True


def test_empty_incomplete():
    assert validate("") == False
    assert validate("123.0") == False