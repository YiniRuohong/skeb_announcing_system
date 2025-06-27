import requests

# Default headers copied from skeb_utils to avoid 403 errors
DEFAULT_HEADERS = {
    "authority": "skeb.jp",
    "pragma": "no-cache",
    "cache-control": "no-cache",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="99", "Microsoft Edge";v="99"',
    "accept": "application/json, text/plain, */*",
    "dnt": "1",
    "authorization": "Bearer null",
    "sec-ch-ua-mobile": "?0",
    "user-agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46"
    ),
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://skeb.jp/",
    "accept-language": "ja,en;q=0.9",
}

class SkebClient:
    def __init__(self, cookie: str):
        self.session = requests.Session()
        self.session.headers.update(DEFAULT_HEADERS)
        if cookie:
            self.session.headers['Cookie'] = cookie

    def get_user(self, name: str):
        """Fetch user information."""
        url = f'https://skeb.jp/api/users/{name.lstrip("@")}'
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def get_following(self):
        """Return a list of creators the current user follows."""
        me = self.get_user('me')
        my_name = me.get('screen_name')
        url = f'https://skeb.jp/api/users/{my_name}/followings'
        data = self.session.get(url)
        data.raise_for_status()
        creators = data.json().get('following_creators', [])
        results = []
        for c in creators:
            info = self.get_user(c['screen_name'])
            c['skills'] = info.get('skills', [])
            c['acceptable'] = info.get('acceptable')
            results.append(c)
        return results
