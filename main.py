from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputAudioStream
from yt_dlp import YoutubeDL

api_id = 20955666
api_hash = "a5eba0f71ecf9340a52f4a41dfc89e3f"
session = "BQE_whIAxYjjMmzzQC8JNVFefDIR-PUS8Cak4a4EqmgQ_htG6QIuw1zixeeiYfr7vnZ5Au1F6635RU8U67J_QJa_tXlwo5..."

app = Client(session, api_id=api_id, api_hash=api_hash)
vc = PyTgCalls(app)

@app.on_message(filters.command("play") & filters.text)
async def play_audio(client, message):
    query = message.text.split(maxsplit=1)[1]
    with YoutubeDL({'format': 'bestaudio'}) as ydl:
        info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
        url = info['url']
    await vc.join_group_call(
        message.chat.id,
        InputAudioStream(url)
    )

app.start()
vc.start()
print("Bot is running...")
app.idle()
