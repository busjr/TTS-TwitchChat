import json
import os
import asyncio
import queue
from twitchio.ext import commands
from TTS import Speech, SpeechAI
# from dotenv import load_dotenv

# load_dotenv()
# token = os.getenv("token")

with open('src\\config.json') as f:
    file_content = f.read()
    templates = json.loads(file_content)

token = templates["setting"]["token"]

class Bot(commands.Bot):
    # def __init__(self, queue: queue.Queue):
    def __init__(self):
        super().__init__(
            token=token,
            initial_channels=[templates["setting"]["namechannel"]],
            prefix="!",
        )
        # self.queue = queue

    async def event_ready(self):
        msg = f"Connected to chat {templates['setting']['namechannel']}"
        # self.queue.put(msg)
        print(msg)

    async def event_message(self, message):
        if message.echo:
            return
        await self.handle_commands(message)

    async def event_command_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandNotFound):
            return  # Просто игнорируем неизвестные команды

    @commands.command(name='tts')
    async def tts_command(self, ctx):
        # if ctx.author.name in templates["white_list"]:
            msg = f"> {ctx.author.name}: {ctx.message.content}"
            # self.queue.put(msg)
            print(msg)
            if templates["setting"]["voice_mode"] == "AI":
                tts = SpeechAI(templates["white_list"][ctx.author.name])
                tts.speak(ctx.message.content)
            elif templates["setting"]["voice_mode"] == "defalt":
                asyncio.run(Speech(ctx.message.content))
            else:
                asyncio.run(Speech(ctx.message.content))
