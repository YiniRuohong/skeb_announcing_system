import sys
import time
from datetime import datetime
from skeb_monitor.client import SkebClient


def load_artists(path="artists.txt"):
    artists = []
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    artists.append(line.lstrip("@"))
    except FileNotFoundError:
        print(f"artists file not found: {path}", file=sys.stderr)
    return artists


def fetch_with_retries(client, name):
    delay = 1
    for attempt in range(3):
        try:
            return client.get_user(name)
        except Exception as e:
            if attempt == 2:
                ts = datetime.now().strftime("%Y-%m-%d %H:%M")
                print(f"[{ts}] failed to fetch {name}: {e}", file=sys.stderr)
            else:
                time.sleep(delay)
                delay *= 2


def main():
    artists = load_artists()
    client = SkebClient.from_storage("skeb_storage.json")
    status = {}
    while True:
        for name in artists:
            data = fetch_with_retries(client, name)
            if not data:
                continue
            open_now = bool(data.get("acceptable"))
            price = data.get("price")
            prev = status.get(name)
            if prev is not None:
                prev_open = prev["open"]
                if not prev_open and open_now:
                    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
                    print(f"[{ts}] {name} opened commissions – ¥{price}")
                elif prev_open and not open_now:
                    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
                    print(f"[{ts}] {name} closed commissions")
            status[name] = {"open": open_now, "price": price}
        time.sleep(1800)


if __name__ == "__main__":
    main()
