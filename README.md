# Nextbike API wrapper (unofficial)

This is an unofficial [nextbike](https://www.nextbike.net/) API client.

It's worthy to note, that the API itself isn't open, so there is no permission of use or SLA.

Currently, the client implements only read operations.

### How to run the tests

There are two kinds of tests here: unit tests and integration tests. First ones do their job without interaction with some external stuff, e. g. Nextbike API.
The latter need to make use of some external API. That makes them more time-consuming.

To be able to run tests, you need to install development packages:
```
$ pipenv install --dev
```

So, to run unit tests you need to execute `pytest`

But if you want to perform deep tests, you need to set a relevant environment variable:
```
export NEXTBIKE_API_SKIP_INTEGRATION_TESTS=False
```
and then run the tests:
```
pytest
```
