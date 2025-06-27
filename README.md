# skeb_announcing_system
一个自动通知和发送申请的skeb画师监控系统

## Development Roadmap
See [TASKS.md](TASKS.md) for the planned tasks and implementation steps.

## Running the server

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Export your cookie and start the server:
   ```bash
   export SKEB_COOKIE="_session=..."
   python -m skeb_monitor.server
   ```
3. Open `frontend/index.html` in your browser.
