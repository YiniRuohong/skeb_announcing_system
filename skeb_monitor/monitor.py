import os
import smtplib
from email.mime.text import MIMEText
from typing import List

from .client import SkebClient
from . import Config

class Monitor:
    def __init__(self, client: SkebClient):
        self.client = client
        self.last_open: List[str] = []

    def check(self):
        artists = self.client.get_following()
        open_artists = []
        for artist in artists:
            if artist.get('acceptable'):
                open_artists.append(artist)
        newly_open = [a for a in open_artists if a['screen_name'] not in self.last_open]
        if newly_open:
            self.notify(newly_open)
        self.last_open = [a['screen_name'] for a in open_artists]
        return open_artists

    def notify(self, artists):
        body = '\n'.join(f"{a['name']} (@{a['screen_name']}) is now open" for a in artists)
        msg = MIMEText(body)
        msg['Subject'] = 'Skeb artists opened commissions'
        msg['From'] = Config.EMAIL_FROM
        msg['To'] = Config.EMAIL_TO

        with smtplib.SMTP(Config.EMAIL_HOST, Config.EMAIL_PORT) as s:
            s.send_message(msg)

if __name__ == '__main__':
    cookie = os.getenv('SKEB_COOKIE', Config.SKB_COOKIE)
    client = SkebClient(cookie)
    monitor = Monitor(client)
    print(monitor.check())
