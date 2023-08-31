import requests


BASE_URL_PLACEHOLDER = 'https://jsonplaceholder.typicode.com'
class Placeholder_API:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_request(self, endpoint):
        url = f'{self.base_url}/{endpoint}'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_all_posts(self):
        return self.get_request('users/1/posts')

    def get_one_post(self, number):
        return self.get_request(f'posts/{number}')

    def get_all_photos(self):
        return self.get_request('albums/1/photos')

    def get_all_comments(self):
        return self.get_request('posts/1/comments')

    def get_one_comment(self, number):
        return self.get_request(f'comments/{number}')

