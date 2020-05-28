"""Test URLs against Google Safe Browsing API."""

import requests

# from safe_browsing.ifx.configuration import get_value
import safe_browsing.ifx.configuration as config


API_KEY = config.get_value('API_KEY')
API_BASE_URL = 'https://safebrowsing.googleapis.com/v4/threatMatches:find?'
API_URL = API_BASE_URL + f'key={API_KEY}'

CLIENT_DATA = {
    "clientId": "ryanproject",
    "clientVersion": "0.0.1",
}

THREAT_INFO = {
    "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
    "platformTypes": ["WINDOWS"],
    "threatEntryTypes": ["URL"],
    "threatEntries": [],
}

PAYLOAD = {
    "client": CLIENT_DATA,
    "threatInfo": THREAT_INFO,
}


def call_api(url_to_check):
    """Check url against safe browsing API."""
    entry = {'url': url_to_check}
    PAYLOAD['threatInfo']['threatEntries'].append(entry)
    return requests.post(API_URL, json=PAYLOAD)
