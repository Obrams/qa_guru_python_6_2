import pytest


@pytest.fixture
def browser():
    print("Браузер стартует!")

    yield
    print("Браузер закрывается!")


@pytest.fixture
def chrome():
    pass


@pytest.fixture
def user_id():
    return 123


def test_aut(user_id):
    assert user_id == 123
