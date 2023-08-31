import requests


BASE_URL_BREW = 'https://api.openbrewerydb.org/v1'
class Brew_API:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_request(self, endpoint):
        url = f'{self.base_url}/{endpoint}'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_single_brewery(self, ob_id):
        return self.get_request(f'/breweries/{ob_id}')

    def get_list_brewery_by_city(self, city):
        return self.get_request(f'/{city}')

    def get_random_brewery(self, ):
        return self.get_request('/breweries/random')

    def get_random_brewery_by_size(self):
        return self.get_request(f'/breweries/random?size=5')


    def list_by_state(self):
        return self.get_request(f'/breweries?by_state=bute&per_page=1')
