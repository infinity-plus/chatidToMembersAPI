from os import getenv

from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from telethon.sync import TelegramClient

TOKEN: str = getenv("TOKEN", "")
API_ID: int = int(getenv("API_ID", "0"))
API_HASH: str = getenv("API_HASH", "")
client = TelegramClient("bot", API_ID, API_HASH)
app = FastAPI(title="Telegram ChatID to Chat Members API")


@app.get("/{chat_id}", response_class=UJSONResponse)
async def mention_list(chat_id: int):
    chat_members = None
    my_client = await client.start(bot_token=TOKEN)
    async with my_client:
        chat_members = await my_client.get_participants(chat_id)
    return {user.id: user.first_name for user in chat_members}
