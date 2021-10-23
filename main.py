from os import getenv
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

TOKEN: str = getenv("TOKEN", "")
API_ID: int = int(getenv("API_ID", "0"))
API_HASH: str = getenv("API_HASH", "")
client = TelegramClient(StringSession(getenv("STRING_SESSION")), API_ID, API_HASH)
app = FastAPI(title="Telegram ChatID to Chat Members API")


@app.get("/", response_class=UJSONResponse)
def root():
    return {"success": True}


@app.get("/get/{chat_id}", response_class=UJSONResponse)
async def mention_list(chat_id: int):
    global client
    client1 = await client.start(TOKEN)
    chat_members = client1.iter_participants(chat_id)
    return {user.id: user.first_name async for user in chat_members}
