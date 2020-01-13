import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_first_program():
    message = "Hello"
    assert message == "Hello"


@pytest.mark.xfail
def test_first_program_Cart1():
    message = "Hello1"
    assert message == "Hello1"
