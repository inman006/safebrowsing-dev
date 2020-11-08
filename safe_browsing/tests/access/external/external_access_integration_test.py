"""This is where you would write your tests."""

import dacite
import pytest

import safe_browsing.access.external.contracts as contracts
import safe_browsing.access.external.service as external_access
import safe_browsing.tests.helpers.request_builder as request_builder


@pytest.mark.parametrize(
    'arg, expected',
    [
        (
            ['www.google.com', 'www.youtube.com'],
            {'safe': ['www.google.com', 'www.youtube.com'], 'unsafe': []}
        ),
        (
            ['http://malware.testing.google.test/testing/malware/'],
            {'safe': [], 'unsafe': ['http://malware.testing.google.test/testing/malware/']}
        ),
    ]
)
def test_access(arg, expected):
    """Test external_access."""
    # Arrange ----------------------------------------------------------------
    safe_browsing_request = request_builder.build(arg)
    # Act --------------------------------------------------------------------
    response = external_access.call_api(safe_browsing_request)
    # Assert -----------------------------------------------------------------
    assert response.safe_urls == expected['safe']
    assert response.unsafe_urls == expected['unsafe']
