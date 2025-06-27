import requests

class SkebClient:
    def __init__(self, cookie: str):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0',
            'Accept': 'application/json, text/plain, */*',
            'Referer': 'https://skeb.jp/'
        })
        if cookie:
            self.session.headers['Cookie'] = cookie

    def get_user(self, name: str):
        url = f'https://skeb.jp/api/users/{name.lstrip("@")}'
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def get_following(self):
        url = 'https://skeb.jp/api/followings'
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()
