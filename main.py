from pyrogram import Client
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types.stream import StreamAudioEnded
from pytgcalls.types.input_stream import InputAudioStream
import yt_dlp

api_id = 20955666
api_hash = "a5eba0f71ecf9340a52f4a41dfc89e3f"
session = "BQE_whIAxYjjMmzzQC8JNVFefDIR-PUS8Cak4a4EqmgQ_htG6QIuw1zixeeiYfr7vnZ5Au1F6635RU8U67J_QJa_tXIwo5_pVZmf4FtwJLMO6rva9aR4dh7V467r8MDcqxoyNKJ3g_eErpKOl_WsV5ctnUxbweqnwBO5OjF9VO7Te4TJJEfpU55E-R25Kcq80Vzy9uS3Z7HZ9PPL6K87fP2rMGGk1iTI1JLX3seZ-takrvT0-pD1g--GMK_hJf0SJyvza2LvKg7gqr4NuA2mPT6F29PLHddj15DPqDn74-MACgMDDJaT5ExLL1oLaT0gWGrK8-CE4pJCzbRpaW1yq-FIrl2hcwAAAAGyPxo3AA"

app = Client(session, api_id=api_id, api_hash=api_hash)
vc = PyTgCalls(app)

@app.on_message()
async def play_audio(client, message):
    if message.text.startswith("/play"):
        query = message.text.split(maxsplit=1)[1]
        ydl_opts = {'format': 'bestaudio'}
        info = yt_dlp.YoutubeDL(ydl_opts).extract_info(f"ytsearch:{query}", download=False)['entries'][0]
        url = info['url']
        
        await vc.join_group_call(
            message.chat.id,
            InputAudioStream(
                url,
            ),
        )
        await message.reply_text(f"🔊 Playing: {info['title']}")

@vc.on_stream_end()
async def on_stream_end(client: PyTgCalls, update: Update):
    chat_id = update.chat_id
    await vc.leave_group_call(chat_id)
    print(f"Left voice chat in {chat_id} because stream ended.")

app.start()
vc.start()
print("Bot is running...")
app.idle()
