from week_1.bank import value


def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0


def test_just_h():
    assert value("hey") == 20
    assert value("h") == 20


def test_other():
    assert value("ahoy") == 100


def test_empty():
    assert value("") == 100

def test_numbers():
    assert value("123") == 100