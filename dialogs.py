import asyncio
from telethon import TelegramClient
from config import API_ID,API_HASH

async def main():
    client = TelegramClient("userBot",API_ID,API_HASH)
    await client.start()
    dialogs = await client.get_dialogs(limit=10,ignore_pinned =True)

    bots = []
    groups = []
    channels = []
    users = []
    for dialog in dialogs:
        title = dialog.title
        if getattr(dialog.entity,'bot',None):
            bots.append(dialog)
        elif dialog.is_group:
            groups.append(dialog)
        elif dialog.is_channel:
            channels.append(dialog)
        else:
            users.append(dialog)

    print(bots)
    print(groups)
    print(channels)
    print(users)

    for user in users:
        if user.title == 'Telegram' and user.id == 777000:
            await user.send_message('hello Telegram')
        elif user.title == 'Mohammadreza Jafari':
            await user.send_message('hello Mohammadreza')
            # await user.delete()

    await client.run_until_disconnected()

asyncio.run(main())