from pyrogram import Client
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputAudioStream
import yt_dlp

api_id = 12345678  # Replace with your API ID
api_hash = "your_api_hash_here"  # Replace with your API HASH
session = "your_string_session_here"  # Replace with your String Session

app = Client(session, api_id=api_id, api_hash=api_hash)
vc = PyTgCalls(app)

@app.on_message()
async def play_audio(client, message):
    if message.text.startswith("/play"):
        query = message.text.split(maxsplit=1)[1]
        info = yt_dlp.YoutubeDL({'format': 'bestaudio'}).extract_info(query, download=False)
        url = info['url']
        await vc.join_group_call(
            message.chat.id,
            InputAudioStream(
                url
            )
        )

app.start()
vc.start()
print("Bot is running...")
app.idle()
