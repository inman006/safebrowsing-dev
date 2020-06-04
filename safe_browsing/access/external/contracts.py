"""External access contracts."""

from dataclasses import dataclass
from typing import List

@dataclass
class ThreatTypes:
    """Threat types to check."""

    malware: bool
    social_engineering: bool

@dataclass
class SafeBrowsingRequest:
    """Encapsulate all aspects of a Safe Browsing request."""

    threat_types: ThreatTypes
    threat_entries:  List[str]
