"""This is where you would write your tests."""

from dataclasses import dataclass
import safe_browsing.access.external.service as external_access
import dacite
import safe_browsing.access.external.contracts as contracts


def test_safe():  # noqa:  D103
    # Arrange ----------------------------------------------------------------
    payload = dict(
        malware=True,
        social_engineering=True,
    )
    threat_types = dacite.from_dict(contracts.ThreatTypes, payload)
    threat_entries = [
        "www.google.com",
        "www.youtube.com",
    ]
    payload = dict(
        threat_types=threat_types,
        threat_entries=threat_entries,   
    )
    safe_browsing_request = dacite.from_dict(contracts.SafeBrowsingRequest, payload)
    # Act --------------------------------------------------------------------
    # breakpoint()
    response = external_access.call_api(safe_browsing_request)
    # Assert -----------------------------------------------------------------
    assert safe_urls = urls_to_check  # all urls to check are safe
    


def test_unsafe():  # noqa:  D103
    # Arrange ----------------------------------------------------------------
    payload = dict(
        malware=True,
        social_engineering=True,
    )
    threat_types = dacite.from_dict(contracts.ThreatTypes, payload)
    threat_entries = [
        'http://malware.testing.google.test/testing/malware/'
    ]
    payload = dict(
        threat_types=threat_types,
        threat_entries=threat_entries,   
    )
    safe_browsing_request = dacite.from_dict(contracts.SafeBrowsingRequest, payload)
    # Act --------------------------------------------------------------------
    response = external_access.call_api(safe_browsing_request)
    # Assert -----------------------------------------------------------------
    assert response.ok  # Still 200 response
    assert response.json()  # The result should not be empty
