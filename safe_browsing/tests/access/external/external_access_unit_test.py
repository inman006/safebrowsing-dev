"""This is where you would write your tests."""


import safe_browsing.access.external.service as external_access


def test_safe():  # noqa:  D103
    # Arrange ----------------------------------------------------------------
    url_to_check = 'https://www.google.com'
    # Act --------------------------------------------------------------------
    response = external_access.call_api(url_to_check)
    # Assert -----------------------------------------------------------------
    assert response.ok  # 200 response
    assert not response.json()  # An empty dict is good


def test_unsafe():  # noqa:  D103
    # Arrange ----------------------------------------------------------------
    url_to_check = 'http://malware.testing.google.test/testing/malware/'
    # Act --------------------------------------------------------------------
    response = external_access.call_api(url_to_check)
    # Assert -----------------------------------------------------------------
    assert response.ok  # Still 200 response
    assert response.json()  # The result should not be empty


def test_synntax_errer():  # noqa:  D103
    # Arrange ----------------------------------------------------------------
    url_to_check = 0  # This is not a string; i.e., invalid url
    # Act --------------------------------------------------------------------
    response = external_access.call_api(url_to_check)
    # Assert -----------------------------------------------------------------
    assert not response.ok  # 400 response
