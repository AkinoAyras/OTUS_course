import pytest
from hw4.fixtures.dogs import *


@pytest.fixture()
def api():
    return Dogs_API(BASE_URL_DOGS)


def test_all_breeds(api):
    response = api.get_all_breeds()
    assert response['status'] == 'success'


def test_random_image(api):
    response = api.get_all_breeds()
    assert response['status'] == 'success'


breeds = ['akita', 'borzoi', 'havanese']
@pytest.mark.parametrize('breed', breeds)
def test_by_breed(api, breed):
    response = api.get_by_breed(breed)
    assert response['status'] == 'success'

@pytest.mark.parametrize('number', ['1', '10', '35'])
def test_by_several_numbers(api, number):
    response = api.get_by_several_numbers(number)
    assert response['status'] == 'success'

@pytest.mark.parametrize('breed', ['hound'])
def test_by_subbreed(api, breed):
    response = api.get_by_subbreed(breed)
    assert response['status'] == 'success'

