"""This is where you would write your tests."""

import dacite

import safe_browsing.access.external.service as external_access
import safe_browsing.access.external.contracts as contracts


def test_safe():  # noqa:  D103
    # Arrange ----------------------------------------------------------------
    threat_entries = [
        "www.google.com",
        "www.youtube.com",
    ]
    payload = dict(
        threat_entries=threat_entries,
    )
    safe_browsing_request = dacite.from_dict(
        contracts.SafeBrowsingRequest,
        payload,
    )
    # Act --------------------------------------------------------------------
    response = external_access.call_api(safe_browsing_request)
    # Assert -----------------------------------------------------------------
    assert response.safe_urls == threat_entries
    assert response.unsafe_urls == []


def test_unsafe():  # noqa:  D103
    # Arrange ----------------------------------------------------------------
    threat_entries = [
        'http://malware.testing.google.test/testing/malware/'
    ]
    payload = dict(
        threat_entries=threat_entries,
    )
    safe_browsing_request = dacite.from_dict(
        contracts.SafeBrowsingRequest,
        payload,
        )
    # Act --------------------------------------------------------------------
    response = external_access.call_api(safe_browsing_request)
    # Assert -----------------------------------------------------------------
    assert response.safe_urls == []
    assert response.unsafe_urls == threat_entries
