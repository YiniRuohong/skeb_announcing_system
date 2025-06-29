# skeb_announcing_system
一个自动通知和发送申请的skeb画师监控系统

## Development Roadmap
See [TASKS.md](TASKS.md) for the planned tasks and implementation steps.

## Running the server

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Export your cookie and start the server. The cookie only needs the
   `request_key` value provided after logging in:
   ```bash
   export SKEB_COOKIE="request_key=YOUR_VALUE"
   python -m skeb_monitor.server
   ```
3. **Open the site using the server URL**. Do not load `index.html` directly
   from disk or the API calls will fail. Instead browse to
   `http://localhost:5000/`.

The page lists the artists you follow and shows whether they are accepting
commissions. Each entry includes a button that opens the artist's Skeb page in a
new tab.

## Getting cookies with a browser

If you prefer obtaining the full cookie via a browser, run:

```bash
python login_browser.py
```

A Chrome window opens so you can log in via Twitter/X. After logging in,
press Enter in the console to save the cookies to `skeb_storage.json`.

## Command-line monitoring

You can monitor selected artists using `monitor_manual.py`. Create an
`artists.txt` listing their screen names (one per line) and run:

```bash
python monitor_manual.py
```

