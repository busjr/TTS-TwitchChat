import threading
import asyncio
import os
import logging
from ChatTwitchio import Bot

if __name__ == '__main__':
    logging.disable(logging.CRITICAL)

    def run_bot():
        asyncio.run(bot.run())

    bot = Bot()
    thread = threading.Thread(target=run_bot)
    thread.start()

    os.system("CLS")
    print("### TTS TwitchChat ###")
    print("Press Ctrl+C to stop")
    try:
        thread.join()
    except KeyboardInterrupt:
        print("The program was stopped by the user")

    
