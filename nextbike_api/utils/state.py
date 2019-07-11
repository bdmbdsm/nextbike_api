import os

SKIP_INTEGRATION_TESTS = 'NEXTBIKE_API_SKIP_INTEGRATION_TESTS'

def skip_integration_tests():
    return os.environ.get(SKIP_INTEGRATION_TESTS, True)
