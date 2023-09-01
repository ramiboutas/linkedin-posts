import pytest
from linkedin_posts import get_access_token


def test_get_access_token():
    assert False == False


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()
