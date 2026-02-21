# TTS-TwitchChat

[RU Русский](<README (ru).md>) | [EN English](<README.md>)

---

## RU Русский

Озвучка чата Twitch в реальном времени для (RU, ENG) языков. Бот подключается к Twitch‑чату и озвучивает сообщения командой `!tts` с помощью двух вариантов синтеза речи:
- `edge-tts` — нейросинтез Microsoft  
- `tts_with_rvc` — использование AI‑голосов с сайта [weights.com](https://www.weights.com/ru/models) (голоса помещать в папку проекта "models")

Для чтения чата используется библиотека [TwitchIO](https://twitchio.dev/).

### Установка

0. [Скачайте Python 3.12.4](https://www.python.org/downloads/release/python-3124/)

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
```bash
venv\Scripts\activate.bat
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
5. **Установите ffmpeg в системные переменные path**

   • Скачайте [ffmpeg](https://www.gyan.dev/ffmpeg/builds/packages/ffmpeg-7.0.2-full_build.7z) или скачайте архив в releases он там будет

   • Переместите разархивированную папку рядом с файлом "add ffmpeg.py"

   • Запустите ("add ffmpeg.py") от Администратора

6. **Установите VLC media player** (нужен для воспроизведения звука)
 - <https://www.videolan.org/vlc/>

### Настройка

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

### Запуск

```bash
python "src\main (CMD).py"
```


---



