import requests
from urllib.parse import urlencode
from nextbike_api.exceptions import NotAllowedQueryKey

class Client:

    _allowed_url_params = ('countries',)

    def __init__(self):
        self._base_url = 'https://api.nextbike.net/maps/nextbike-official.json'

    def _build_url(self, *args, **kwargs):
        self._check_allowed_query_keys(kwargs)
        params = urlencode(kwargs)
        return '{0}?{1}'.format(self._base_url, params)

    def _check_allowed_query_keys(self, params):
        for param in params.keys():
            if param not in self._allowed_url_params:
                raise NotAllowedQueryKey(
                    'Bad query param: {0}'.format(param)
                )

    def all_countries(self):
        url = self._build_url()
        resp = requests.get(url)
        return resp.json()

    def country(self, country_code):
        url = self._build_url(countries=country_code)
        resp = requests.get(url)
        return resp.json()
