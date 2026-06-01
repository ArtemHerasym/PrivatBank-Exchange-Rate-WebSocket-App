# PrivatBank Exchange Rate WebSocket App

This project is an asynchronous Python application that fetches exchange rates from the PrivatBank API. It includes a console utility and a WebSocket-based web interface.

## Features

* Get USD and EUR exchange rates for the last 1–10 days using the console version
* Add extra currencies through console arguments
* Fetch exchange rates asynchronously using `aiohttp`
* WebSocket web interface with currency checkboxes and day selection
* Async logging of exchange requests using `aiofile` and `aiopath`
* Error handling for invalid input and network/API issues
* Deployed frontend and backend using Netlify and Render

## Technologies Used

* Python
* asyncio
* aiohttp
* websockets
* aiofile
* aiopath
* HTML
* CSS
* JavaScript

## Installation

Clone the repository:

```bash
git clone https://github.com/ArtemHerasym/PrivatBank-Exchange-Rate-WebSocket-App.git
cd PrivatBank-Exchange-Rate-WebSocket-App
```

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Console Usage

Run the console utility:

```bash
python exchange_service_console.py 2
```

This returns USD and EUR exchange rates for the last 2 days.

You can also add extra currencies:

```bash
python exchange_service_console.py 2 GBP PLN CAD
```

The number of days must be from 1 to 10.

## WebSocket Usage

Run the WebSocket server locally:

```bash
python server.py
```

Then open `index.html` in your browser.

For local testing, make sure `main.js` uses:

```js
const ws = new WebSocket("ws://localhost:8080");
```

For the deployed Netlify version, `main.js` should use the Render backend URL:

```js
const ws = new WebSocket("wss://privatbank-exchange-rate-websocket-app.onrender.com");
```

Select currencies, choose the number of days, and click **SHOW EXCHANGE**.

The browser sends a WebSocket request to the server. The server fetches exchange rates from PrivatBank and sends the result back to the page.

## Deployed Version

Frontend is deployed on Netlify.
Backend WebSocket server is deployed on Render.

Live site: `<privatbank-exchange-rate-app.netlify.app>`

Note: Render free services may sleep after inactivity, so the first connection can take 30–60 seconds.

## Logging

Every time the exchange command is used through the WebSocket interface, the program writes a log entry to:

```bash
logs/exchange.log
```

Each log entry contains the time, number of days, and selected currencies.

## Project Structure

```text
project/
├── .gitignore
├── exchange_service_console.py
├── index.html
├── main.js
├── poetry.lock
├── pyproject.toml
├── README.md
├── requirements.txt
├── server.py
└── style.css
```

## Author

Created as a Python async programming project by Artem Herasymenko.
