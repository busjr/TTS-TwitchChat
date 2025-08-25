# 🎙 TTS-TwitchChat

[RU Русский](<README (ru).md>) | [EN English](<README.md>)

---

## EN English

Real‑time Twitch chat TTS for (RU and ENG) messages. The bot connects to a Twitch chat and speaks messages triggered with the `!tts` command using two speech‑synthesis back‑ends:
- `edge-tts` — Microsoft neural TTS  
- `tts_with_rvc` — AI voices downloaded from [weights.com](https://www.weights.com/ru/models) (votes should be placed in the project folder "models")

Chat reading is handled by the [TwitchIO](https://twitchio.dev/) library.

### 📥 Installation

0. [Download Python 3.12.4](https://www.python.org/downloads/release/python-3124/)

1. **Download the project**:
   • ZIP archive from GitHub  
   • or clone via Git:
```bash
git clone https://github.com/busjr/TTS-TwitchChat.git
```

2. **Change into the project folder**
```bash
cd TTS-TwitchChat
```

3. **Create a virtual environment**
```bash
python -m venv venv
```
```bash
venv\Scripts\activate.bat
```

4. **Install dependencies**
```bash
pip install edge-tts==7.0.2
pip install tts_with_rvc==0.1.9.1
pip install python-vlc==3.0.21203
pip install twitchio==2.0.0
```
**or**
```bash
pip install -r requirements.txt
```
5. Add ffmpeg to the system PATH environment variable
  
   • Download [ffmpeg](https://www.gyan.dev/ffmpeg/builds/packages/ffmpeg-7.0.2-full_build.7z) or get the archive from the releases section where it is available

   • Extract the folder and move it next to the "add ffmpeg.py" file

   • Run the "add ffmpeg.py" script as Administrator

6. **Install VLC media player** (required for audio playback):  
👉 <https://www.videolan.org/vlc/>

### ⚙ Configuration

1. **Rename** `config.json.example` → `config.json`

2. **Edit `config.json`**
```json
{
  "white_list": {
    "USER_NICKNAME": "VOICE_FOLDER_NAME"
  },
  "setting": {
    "token": "oauth:YOUR_TWITCH_TOKEN",
    "namechannel": "CHANEK_NAME_TO_READ",
    "voice_mode": "defolt or AI"
  }
}
```

- `white_list` — mapping of users allowed to be voiced with AI and the folder containing the corresponding voice (leave a dash `-` to fall back to Microsoft Edge TTS).  
- `token` — Twitch OAuth token (generate at <https://twitchtokengenerator.com/>).  
- `namechannel` — Twitch channel the bot will read.  
- `voice_mode`  
  - `"defolt"` — use Microsoft Edge TTS  
  - `"AI"` — use RVC AI voices

### 🚀 Run

```bash
python "src\main (CMD).py"
```

---
