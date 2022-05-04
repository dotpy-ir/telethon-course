import asyncio
from telethon import TelegramClient
from config import API_ID,API_HASH
from telethon import events

async def main():
    client = TelegramClient("realBot",API_ID,API_HASH)
    await client.start()


    @client.on(events.ChatAction)
    async def handler(event):

        if event.user_joined:
            user = await event.get_user()
            await event.reply(f'Welcome {user.first_name}')
            await event.delete()
        
        if event.user_left:
            user = await event.get_user()
            await event.reply(f'Bye {user.first_name}')
            await event.delete()

        



    await client.run_until_disconnected()

asyncio.run(main())