import asyncio
from telethon import TelegramClient
from config import API_ID, API_HASH
from telethon import events


async def main():
    client = TelegramClient("realBot", API_ID, API_HASH)
    await client.start()

    @client.on(events.InlineQuery)
    async def handler(event):
        builder = event.builder
        await event.answer([builder.photo(file='dog.jpg')])

    await client.run_until_disconnected()

asyncio.run(main())
