# Clockout Flask App

A sleek, accessible, dark-mode Flask web app for hourly employees to quickly calculate when they need to clock out to avoid exceeding their weekly hour limits.

## What It Does

Enter your current weekly hours and your latest clock-in time. The app tells you exactly when to clock out to stay under your max hours (default is 40.0). Great for managing overtime.

## Features

- Dark-mode UI with modern, minimalist design
- Keyboard-accessible and screen-reader friendly
- Fully responsive (works on desktops, tablets, and phones)
- Secure by default (CSP headers, no JS dependencies)
- Accessible skip link for screen readers
- Includes favicon and inline logo
- Attribution footer with GitHub profile link

## Getting Started

### On macOS/Linux (or Git Bash on Windows):

```bash
git clone https://github.com/ben-reyna/clockout-web-app.git
cd clockout-web-app
pip install flask
flask run
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Tech Stack

- Python 3.x
- Flask
- HTML5 + CSS3 (no JavaScript!)
- Fully self-contained app with local-only assets

## Security & Privacy

This app is secure by design:

- CSP headers block third-party scripts/styles
- No external JS libraries = no dependency bloat or injection vectors
- No personal data collected or stored
- Local-hosted fonts and favicon
- Safe to host internally or externally

## Folder Structure

```
ClockoutFlaskApp/
│
├── static/              # All static assets (favicons, logos)
├── Templates/           # HTML templates (Jinja2)
├── ClockoutFlaskApp.py  # Main Flask app
└── .gitignore           # Properly ignores cache, .db, venv, etc.
```

## Developed By

[bananalogic](https://github.com/ben-reyna)

Made with Onamac Industies, Inc. hourly employees in mind, but built for everyone.
