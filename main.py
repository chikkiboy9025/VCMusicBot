from pyrogram import Client
from pytgcalls import PyTgCalls
from pytgcalls.types.stream import StreamAudioEnded
import yt_dlp

api_id = 20955666  # Replace with your API ID
api_hash = "a5eba0f71ecf9340a52f4a41dfc89e3f"  # Replace with your API HASH
session = "BQE_whIAxYjjMmzzQC8JNVFefDIR-PUS8Cak4a4EqmgQ_htG6QIuw1zixeeiYfr7vnZ5Au1F6635RU8U67J_QJa_tXIwo5_pVZmf4FtwJLMO6rva9aR4dh7V467r8MDcqxoyNKJ3g_eErpKOl_WsV5ctnUxbweqnwBO5OjF9VO7Te4TJJEfpU55E-R25Kcq80Vzy9uS3Z7HZ9PPL6K87fP2rMGGk1iTI1JLX3seZ-takrvT0-pD1g--GMK_hJf0SJyvza2LvKg7gqr4NuA2mPT6F29PLHddj15DPqDn74-MACgMDDJaT5ExLL1oLaT0gWGrK8-CE4pJCzbRpaW1yq-FIrl2hcwAAAAGyPxo3AA"  # Replace with your String Session

app = Client(session, api_id=20955666, api_hash=a5eba0f71ecf9340a52f4a41dfc89e3f)
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
