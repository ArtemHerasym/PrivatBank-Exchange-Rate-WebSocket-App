import asyncio
import logging
import aiofiles
import websockets
import names
from websockets.exceptions import ConnectionClosedOK
import json
from exchange_service_console import get_exchange
from aiofile import async_open
from anyio import Path as AsyncPath
from datetime import datetime

logging.basicConfig(level=logging.INFO)


async def log_exchange_command(days, currencies):
    log_dir = AsyncPath("logs")
    await log_dir.mkdir(exist_ok=True, parents=True)
    log_file = log_dir / "exchange.log"
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"date: {time_now} | days: {days} | currencies: {currencies}\n"
    async with aiofiles.open(log_file, mode="a", encoding="utf-8") as f:
        await f.write(log_line)


class Server:
    clients = set()

    async def register(self, ws):
        ws.name = names.get_full_name()
        self.clients.add(ws)
        logging.info(f"{ws.remote_address} connects")

    async def unregister(self, ws):
        self.clients.remove(ws)
        logging.info(f"{ws.remote_address} disconnects")

    async def send_to_clients(self, message: str):
        if self.clients:
            [await client.send(message) for client in self.clients]

    async def ws_handler(self, ws):
        await self.register(ws)
        try:
            await self.distrubute(ws)
        except ConnectionClosedOK:
            pass
        finally:
            await self.unregister(ws)

    async def distrubute(self, ws):
        async for message in ws:
            request = json.loads(message)
            command = request["command"]
            currencies = request["currencies"]
            days = request["days"]
            if command == "exchange":
                await log_exchange_command(days, currencies)
                result = await get_exchange(days, currencies)
                await ws.send(json.dumps(result, indent=2, ensure_ascii=False))


async def main():
    server = Server()
    async with websockets.serve(server.ws_handler, "localhost", 8080):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
