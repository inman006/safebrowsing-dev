"""Test URLs against Google Safe Browsing API."""

import requests

import dacite

import safe_browsing.ifx.configuration as config
import safe_browsing.access.external.contracts as contracts

API_KEY = config.get_value('API_KEY')
API_BASE_URL = 'https://safebrowsing.googleapis.com/v4/threatMatches:find?'
API_URL = API_BASE_URL + f'key={API_KEY}'

CLIENT_DATA = {
    "clientId": "ryanproject",
    "clientVersion": "0.0.1",
}

THREAT_INFO = {
    "threatTypes": ["MALWARE"],
    "platformTypes": ["WINDOWS"],  # TODO: Add more platforms
    "threatEntryTypes": ["URL"],
    "threatEntries": [],
}

PAYLOAD = {
    "client": CLIENT_DATA,
    "threatInfo": THREAT_INFO,
}


def call_api(safe_browsing_request):
    """
    Check url against safe browsing API.

    The response only contains information regarding unsafe urls
    As a result, we assume all urls in `urls_to_check` are safe until
    we see information in the response telling us it is not.
    """
    urls_to_check = safe_browsing_request.threat_entries
    my_urls = {'url': url for url in urls_to_check}

    PAYLOAD['threatInfo']['threatEntries'] = my_urls
    response_from_requests = requests.post(API_URL, json=PAYLOAD)

    safe_urls = list(urls_to_check)  # Make a copy of urls to check
    response_dict = response_from_requests.json()

    unsafe_urls = list()
    if response_dict:
        for match in response_dict['matches']:
            unsafe_url = match['threat']['url']
            unsafe_urls.append(unsafe_url)
            safe_urls.remove(unsafe_url)
    payload = dict(
      safe_urls=safe_urls,
      unsafe_urls=unsafe_urls,
      )
    safe_browsing_response = dacite.from_dict(
        contracts.SafeBrowsingResponse,
        payload,
        )
    return safe_browsing_response
