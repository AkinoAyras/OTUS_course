import pytest
from hw4.fixtures.placeholder import *


@pytest.fixture()
def api():
    return Placeholder_API(BASE_URL_PLACEHOLDER)

def test_get_all_posts(api):
    response = api.get_all_posts()
    assert len(response) == 10

@pytest.mark.parametrize('number', ['1', '3'])
def test_get_one_post(api, number):
    response = api.get_one_post(number)
    assert len(response) == 4

def test_get_all_photos(api):
    response = api.get_all_photos()
    assert len(response) == 50

def test_get_all_comments(api):
    response = api.get_all_comments()
    assert len(response) == 5

@pytest.mark.parametrize('number', ['1', '3'])
def test_get_one_comment(api, number):
    response = api.get_one_comment(number)
    assert len(response) == 5
