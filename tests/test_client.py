import pytest
from unittest import mock
from nextbike_api import Client
from nextbike_api.exceptions import NotAllowedQueryKey
from nextbike_api.utils.state import skip_integration_tests

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


@pytest.mark.skip(reason='Very time-consuming test')
def test_all_countries():
    c = Client()

    countries_data = c.all_countries()
    assert countries_data.get('countries')


@pytest.mark.skipif(skip_integration_tests(), reason='Integration test')
def test_get_country_data():
    c = Client()

    country_data = c.country('ua')
    assert country_data.get('countries')
