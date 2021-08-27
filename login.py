import asyncio
from telethon import TelegramClient
from config import API_ID,API_HASH

async def main():
    client = TelegramClient("userBot",API_ID,API_HASH)
    await client.start()

    




    await client.run_until_disconnected()

asyncio.run(main())