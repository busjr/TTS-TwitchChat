# 🎙 Twitch TTS

[RU Русский](#-русский) | [EN English](#-english)

---

## RU Русский

Озвучка чата Twitch в реальном времени для (RU, ENG) языков. Бот подключается к Twitch‑чату и озвучивает сообщения командой `!tts` с помощью двух вариантов синтеза речи:
- `edge-tts` — нейросинтез Microsoft  
- `tts_with_rvc` — использование AI‑голосов с сайта [weights.com](https://www.weights.com/ru/models) (голоса помещать в папку проекта "models")

Для чтения чата используется библиотека [TwitchIO](https://twitchio.dev/).

### 📥 Установка

1. **Скачайте проект**  
   • ZIP‑архив с GitHub  
   • или через Git:
```bash
git clone https://github.com/busjr/TTS-TwitchChat.git
```

2. **Перейдите в папку проекта**
```bash
cd TTS-TwitchChat
```

3. **Создайте виртуальную среду**
```bash
python -m venv venv
```

4. **Установите зависимости**
```bash
pip install edge-tts==7.0.2
pip install tts_with_rvc==0.1.9.1
pip install python-vlc==3.0.21203
pip install twitchio==2.0.0
```
**или**
```bash
pip install -r requirements.txt
```

5. **Установите VLC media player** (нужен для воспроизведения звука):  
👉 <https://www.videolan.org/vlc/>

### ⚙ Настройка

1. **Переименуйте файл** `config.json.example` → `config.json`

2. **Отредактируйте `config.json`**
```json
{
  "white_list": {
    "НИКНЕЙМ_ПОЛЬЗОВАТЕЛЯ": "НАЗВАНИЕ_ПАПКИ_С_AI_ГОЛОСОМ"
  },
  "setting": {
    "token": "oauth:ВАШ_ТОКЕН_ТВИЧА",
    "namechannel": "НАЗВАНИЕ_КАНАЛА_ДЛЯ_ЧТЕНИЯ",
    "voice_mode": "defolt или AI"
  }
}
```

- `white_list` — список пользователей, которых можно озвучивать AI‑голосом и папки с голосом (можно указать прочерк, и будет использоваться Microsoft Edge TTS).  
- `token` — OAuth‑токен Twitch (получить: <https://twitchtokengenerator.com/>)  
- `namechannel` — ник канала Twitch для чтения.  
- `voice_mode`  
  - `"defolt"` — использовать Microsoft Edge TTS  
  - `"AI"` — использовать RVC (AI‑голоса)

### 🚀 Запуск

```bash
python "src\main (CMD).py"
```

---

## EN English

Real‑time Twitch chat TTS for (RU and ENG) messages. The bot connects to a Twitch chat and speaks messages triggered with the `!tts` command using two speech‑synthesis back‑ends:
- `edge-tts` — Microsoft neural TTS  
- `tts_with_rvc` — AI voices downloaded from [weights.com](https://www.weights.com/ru/models) (votes should be placed in the project folder "models")

Chat reading is handled by the [TwitchIO](https://twitchio.dev/) library.

### 📥 Installation

1. **Download the project**  
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

5. **Install VLC media player** (required for audio playback):  
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
