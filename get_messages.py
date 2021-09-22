import asyncio
import json
from telethon import TelegramClient
from config import API_ID, API_HASH


async def main():
    client = TelegramClient("userBot", API_ID, API_HASH)
    await client.start()

    USERNAME = 'dotpy_ir'
    IMPORTANT_MESSAGE_ID = 23
    message = await client.get_messages(USERNAME, ids=IMPORTANT_MESSAGE_ID)

    with open(f'{USERNAME}.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(message.to_dict(), default=str))

    USERNAME = 'varzesh3'
    query = 'رونالدو'
    messages = await client.get_messages(USERNAME, search=query, limit=50)

    all_messsages = {}

    for message in messages:
        message_dict = {
            'views': message.views,
            'sender_id': message.sender_id,
            'forwards': message.forwards,
            'messages': getattr(message, 'message', ''),
        }

        all_messsages[message.id] = message_dict

    with open(f'{USERNAME}.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(all_messsages))

    await client.run_until_disconnected()

asyncio.run(main())
