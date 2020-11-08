"""Request builders."""

from typing import List

import dacite

import safe_browsing.access.external.contracts as contracts
from safe_browsing.access.external.contracts import SafeBrowsingRequest


def build(threat_entries: List[str]) -> SafeBrowsingRequest:
    """Build a SafeBrowsingRequest."""
    payload = dict(
        threat_entries=threat_entries,
    )
    safe_browsing_request = dacite.from_dict(
        contracts.SafeBrowsingRequest,
        payload,
    )
    return safe_browsing_request
