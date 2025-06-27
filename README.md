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
