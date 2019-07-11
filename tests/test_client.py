import pytest
from unittest import mock
from nextbike_api import Client
from nextbike_api.exceptions import NotAllowedQueryKey

def test_init():
    c = Client()
    assert hasattr(c, '_base_url')


def test_build_url():
    data = {'countries': 'ua'}

    c = Client()
    url = c._build_url(**data)
    assert url == c._base_url + '?countries=ua'

def test_build_url_with_not_allowed_key():
    data = {'countries': 'ua', 'planet': 'earth'}

    c = Client()
    try:
        url = c._build_url(**data)
    except NotAllowedQueryKey:
        pass
    else:
        assert False, 'exception must be rised'
