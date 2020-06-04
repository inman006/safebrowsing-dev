"""This is where you would write your tests."""

from dataclasses import dataclass
import safe_browsing.access.external.service as external_access
import dacite
from safe_browsing.access.external.contracts import SafeBrowsingRequest, ThreatTypes


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

    response = external_access.call_api(safe_browsing_request)

    # Assert -----------------------------------------------------------------

    assert response.ok  # 200 response
    assert not response.json()  # An empty dict is good


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


def test_synntax_errer():  # noqa:  D103

    # Arrange ----------------------------------------------------------------

    payload = dict(
        malware=True,
        social_engineering=True,
    )

    threat_types = dacite.from_dict(contracts.ThreatTypes, payload)

    threat_entries = [
        0,  # This is not a string; i.e., invalid url
    ]

    payload = dict(
        threat_types=threat_types,
        threat_entries=threat_entries,   
    )

    safe_browsing_request = dacite.from_dict(contracts.SafeBrowsingRequest, payload)

    # Act --------------------------------------------------------------------

    response = external_access.call_api(safe_browsing_request)

    # Assert -----------------------------------------------------------------

    assert not response.ok  # 400 response
