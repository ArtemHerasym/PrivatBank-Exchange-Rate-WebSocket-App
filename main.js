console.log("Page loaded");

const ws = new WebSocket("wss://privatbank-exchange-rate-websocket-app.onrender.com");

const form = document.getElementById("formChat");
const resultField = document.getElementById("exchange-rate");

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const checkedBoxes = document.querySelectorAll(
    'input[type="checkbox"]:checked',
  );

  const currencies = [];

  checkedBoxes.forEach((box) => {
    currencies.push(box.value);
  });

  const days = document.getElementById("days").value;

  const request = {
    command: "exchange",
    days: Number(days),
    currencies: currencies,
  };

  if (currencies.length === 0) {
    resultField.textContent = "Please select at least one currency.";
    return;
  }

  if (ws.readyState !== WebSocket.OPEN) {
  resultField.textContent = "Server is still connecting. Wait a few seconds and try again.";
  return;
}

  ws.send(JSON.stringify(request));

  resultField.textContent = "Loading...";
});

ws.onopen = () => {
  console.log("Connected to WebSocket server");
  resultField.textContent = "Connected. Select options and click SHOW EXCHANGE.";
};

ws.onmessage = (event) => {
  resultField.textContent = event.data;
};

ws.onerror = () => {
  resultField.textContent = "WebSocket connection error";
};

ws.onclose = () => {
  resultField.textContent =
    "WebSocket connection closed. The Render server may be sleeping. Refresh the page and wait a few seconds.";
};
