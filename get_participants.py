import asyncio
from telethon import TelegramClient
from config import API_ID, API_HASH


async def main():
    client = TelegramClient("userBot", API_ID, API_HASH)
    await client.start()

    users = await client.get_participants("gp_telethon", limit=10, aggressive=True)
    print(users)

    await client.download_media(users[0], "user1.png")

    await client.run_until_disconnected()

asyncio.run(main())
