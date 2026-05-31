# PrivatBank Exchange Rate WebSocket App

This project is an asynchronous Python application that fetches exchange rates from the PrivatBank API. It includes both a console utility and a WebSocket-based web interface.

## Features

- Get USD and EUR exchange rates for the last 1–10 days(console version)
- Add extra currencies through console arguments
- Fetch exchange rates asynchronously using `aiohttp`
- WebSocket web interface with currency checkboxes and day selection
- Async logging of exchange requests using `aiofile` and `aiopath`
- Error handling for invalid input and network/API issues

## Technologies Used

- Python
- asyncio
- aiohttp
- websockets
- aiofile
- aiopath
- HTML
- CSS
- JavaScript

## Installation

Clone the repository:

```bash
git clone <PrivatBank-Exchange-Rate-WebSocket-App>
cd <project-folder>
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

Run the WebSocket server:

```bash
python server.py
```

Then open `index.html` in your browser.

Select currencies, choose the number of days, and click **SHOW EXCHANGE**.

The browser sends a WebSocket request to the server, the server fetches exchange rates from PrivatBank, and the result is displayed on the page.

## Logging

Every time the exchange command is used through the WebSocket interface, the program writes a log entry to:

```bash
logs/exchange.log
```

Each log entry contains the time, number of days, and selected currencies.

## Project Structure

```text
project/
├── main.py
├── server.py
├── exchange_service.py
├── index.html
├── main.js
├── style.css
├── requirements.txt
├── logs/
└── README.md
```

## Author

Created as a Python async programming project by Artem Herasymenko.
