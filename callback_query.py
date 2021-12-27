import asyncio
from telethon import TelegramClient, events, Button
from config import API_ID, API_HASH, TOKEN


async def start_handler(event):
    buttons = [
        [Button.inline("Song", "song.mp3")],
        [Button.inline("Picture", "dog.jpg")],
    ]
    await event.client.send_message(event.chat_id, "start", buttons=buttons)


async def inline_handler(event):
    data = event.data.decode()
    print(data)
    # await event.client.send_message(event.chat_id, data, file=data)
    await event.answer("clicked", alert=True)


async def main():
    client = TelegramClient("realBot", API_ID, API_HASH)
    await client.start(bot_token=TOKEN)

    client.add_event_handler(
        inline_handler, events.CallbackQuery(pattern="song.+"))
    client.add_event_handler(
        start_handler, events.NewMessage(pattern="/start"))

    await client.run_until_disconnected()

asyncio.run(main())
