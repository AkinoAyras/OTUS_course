import pytest
from hw4.fixtures.brewery import *


@pytest.fixture()
def api():
    return Brew_API(BASE_URL_BREW)

def test_get_random_brewery(api):
    response = api.get_random_brewery()
    assert len(response) == 1

@pytest.mark.parametrize('ob_id', ['86531644-17de-4385-af71-82574666baa6', 'ef48afa5-9ac1-439c-851d-0fb04b43786f'])
def test_get_single_brewery(api, ob_id):
    response = api.get_single_brewery(ob_id)
    assert len(response) == 16


@pytest.mark.parametrize('city', ['breweries?by_city=vitrolles&per_page=1', 'breweries?by_city=zipf&per_page=1', 'breweries?by_city=faro&per_page=1'])
def test_get_list_brewery_by_city(api, city):
    response = api.get_list_brewery_by_city(city)
    assert len(response) == 1

def test_get_random_brewery_by_size(api):
    response = api.get_random_brewery_by_size()
    assert len(response) == 5

def test_list_by_state(api):
    response = api.list_by_state()
    assert len(response) == 1

