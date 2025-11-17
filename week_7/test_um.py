import pytest
from week_7.um import count

def test_one_um():
    assert count("um") == 1


def test_punctuation():
    assert count("um?") == 1


def test_um_words():
    assert count("um, thanks for the album") == 1


def test_many_ums():
    assert count("um, thanks, um") == 2