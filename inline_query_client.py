import asyncio
from telethon import TelegramClient
from config import API_ID, API_HASH


async def main():
    client = TelegramClient("userBot", API_ID, API_HASH)
    await client.start()

    MYBOT = "@gif"
    result = await client.inline_query(MYBOT, " ")
    print(result)

    await client.run_until_disconnected()

asyncio.run(main())
