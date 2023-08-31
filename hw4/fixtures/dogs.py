import requests


BASE_URL_DOGS = 'https://dog.ceo/api'
class Dogs_API:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_request(self, endpoint):
        url = f'{self.base_url}/{endpoint}'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_all_breeds(self):
        return self.get_request('breeds/list/all')

    def get_random_image(self):
        return self.get_request('breeds/image/random')

    def get_by_breed(self, breed):
        return self.get_request(f'breed/{breed}/images')

    def get_by_several_numbers(self, number):
        return self.get_request(f'breeds/image/random/{number}')

    def get_by_subbreed(self, breed):
        return self.get_request(f'breed/{breed}/list')
