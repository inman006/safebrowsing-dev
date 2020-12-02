"""External access integration test suite."""

import dacite
import pytest

import safe_browsing.access.external.contracts as contracts
import safe_browsing.access.external.service as external_access
import safe_browsing.tests.helpers.request_builder as request_builder


# Globals --------------------------------------------------------------------


SAFE_TEST_CASE = dict(
    arg=['www.google.com', 'www.youtube.com'],
    expected={
        'safe': ['www.google.com', 'www.youtube.com'],
        'unsafe': [],
    },
)

UNSAFE_TEST_CASE = dict(
    arg=['http://malware.testing.google.test/testing/malware/'],
    expected={
        'safe': [],
        'unsafe': ['http://malware.testing.google.test/testing/malware/'],
    },
)


# Fixtures -------------------------------------------------------------------


@pytest.fixture(params=[SAFE_TEST_CASE, UNSAFE_TEST_CASE])
def access_test_cases(request):
    """External access test cases."""
    return request.param


# Tests ----------------------------------------------------------------------


def test_access(access_test_cases):
    """Test external_access."""
    # Arrange ----------------------------------------------------------------
    safe_browsing_request = request_builder.build(access_test_cases['arg'])
    # Act --------------------------------------------------------------------
    response = external_access.call_api(safe_browsing_request)
    # Assert -----------------------------------------------------------------
    assert response.safe_urls == access_test_cases['expected']['safe']
    assert response.unsafe_urls == access_test_cases['expected']['unsafe']
