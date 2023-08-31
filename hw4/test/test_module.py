import requests


def test_custom_url_status(url, status_code):
    response = requests.get(url)
    assert response.status_code == int(status_code)