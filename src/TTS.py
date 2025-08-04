import os
import time
import edge_tts
from tts_with_rvc import TTS_RVC
import vlc

def play_audio_file(filepath):
    player = vlc.MediaPlayer(filepath)
    player.play()

    time.sleep(0.1)

    while player.get_state() in (vlc.State.Opening, vlc.State.Buffering, vlc.State.Playing):
        time.sleep(0.1)

    return
class SpeechAI:
    def __init__(self, namemodel):
        self.tts = TTS_RVC(
            model_path=f"src\\models\\{namemodel}\\model.pth",
            index_path=f"src\\models\\{namemodel}\\model.index"
        )

    def speak(self, message: str):
        path = self.tts(text=message[4:], pitch=6, index_rate=0.9)
        play_audio_file(path)
        os.remove(path)

async def Speech(message: str):
    folder = 'src\\temp'
    os.makedirs(folder, exist_ok=True)
    filename = os.path.join(folder, 'output.mp3')

    voice = "ru-RU-DmitryNeural"
    communicate = edge_tts.Communicate(text=message[4:], voice=voice)
    await communicate.save(filename)
    play_audio_file(filename)
    os.remove(filename)