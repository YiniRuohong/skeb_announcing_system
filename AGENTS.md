# Agent Instructions

This repository contains a Skeb monitoring system built with Python and Flask. The frontend is a plain React app served by the Flask server.

## Setup
- Install dependencies with `pip install -r requirements.txt` using Python 3.8 or newer.
- Export `SKEB_COOKIE` with your Skeb login cookie (`request_key=` value) before running any server commands.
- Start the development server using `python -m skeb_monitor.server`.
- The web interface will be available at `http://localhost:5000/`.

## Repository Layout
- `skeb_monitor/` – Python package with the server and monitoring logic.
- `frontend/` – Static React files (`index.html` and `app.js`).
- `TASKS.md` – Lists the planned development tasks.

## Development Guidelines
- Place new server features in `skeb_monitor/`.
- Keep the frontend simple; it uses React from the CDN and no build step.
- When changing functionality, update the documentation accordingly.

## Commit and PR Guidelines
- Use concise commit messages in the imperative mood.
- Reference relevant tasks from `TASKS.md` when applicable.
- Summarize your changes clearly in the pull request description.

## Testing
- There are currently no automated tests.
- Before creating a pull request, ensure that `python -m skeb_monitor.server` starts without errors.
