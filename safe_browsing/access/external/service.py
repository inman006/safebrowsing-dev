"""Test URLs against Google Safe Browsing API."""

import requests

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


def call_api(safe_browsing_request):
    """Check url against safe browsing API."""
    urls_to_check = safe_browsing_request.threat_entries
    # Use list comprehension here
    breakpoint()
    my_urls = {url: url for urls in urls_to_check}
    # my_urls = list()
    # for url in urls_to_check:  # grab one widget and go around the track
    #     payload = dict(url=url)  # Do something with the widget
    #     my_urls.append(payload)  # Put the result in the bag and look for the next one
    PAYLOAD['threatInfo']['threatEntries'] = my_urls
    response_from_requests = requests.post(API_URL, json=PAYLOAD)
    # The response only contains information regarding unsafe urls
    # As a result, we assume all urls in `urls_to_check` are safe until
    # we see information in the response telling us it is not.
    safe_urls = list(urls_to_check)  # Make a copy of urls to check
    response_dict = response_from_requests.json()  # potentially contains info regarding unsafe urls
    # So go through each thing in the dict using a loop and remove and append
    # DOn't tryu to use a list comprehension here!
    unsafe_urls = list()
    for match in response_dict['matches']:  # debug
        unsafe_url = match['threat']['url']
        unsafe_urls.appned(unsafe_url)
        safe_urls.revove(unsafe_url)
    payload = dict(
      safe_urls=safe_urls,
      unsafe_urls=unsafe_urls,
      )
    # use the response_from_requests to build a concretion of a SafeBrowsingResponse
    return response_from_requests
    
