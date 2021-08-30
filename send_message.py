import asyncio
from telethon import TelegramClient
from config import API_ID, API_HASH

async def main():
    client = TelegramClient("userBot", API_ID, API_HASH)
    await client.start()

    RECIVER = 'me'
    link = 'https://picsum.photos/id/237/200/300'

    await client.send_message(RECIVER, 'this is sample')
    await client.send_message(RECIVER, link)
    await client.send_message(RECIVER, link, link_preview=False)
    await client.send_message(RECIVER, link, file='dog.jpg')
    await client.send_message(RECIVER, link, file=['dog.jpg', 'song.mp3'], force_document=True)
    await client.send_message(RECIVER,'from internet',file=link)

    await client.run_until_disconnected()

asyncio.run(main())