import pytest
from numb3rs import validate


def test_valid_ip():
    assert validate("127.0.0.1") == True
