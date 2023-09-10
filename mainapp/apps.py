from django.apps import AppConfig
import multiprocessing
import os
from .discord_bot import bot


def start_discord_bot():
    bot.run(os.getenv("TOKEN"))

class MainappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "mainapp"

    def ready(self):
        # Start the Discord bot in a separate process
        bot_process = multiprocessing.Process(target=start_discord_bot)
        bot_process.daemon = True
        bot_process.start()