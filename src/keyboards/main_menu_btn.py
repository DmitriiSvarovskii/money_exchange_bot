from aiogram import Bot
from aiogram.types import BotCommand

from src.lexicons import base_text


async def set_main_menu(bot: Bot) -> None:
    main_menu_commands = [
        BotCommand(command=command, description=description)
        for command, description in base_text.commands_text_dict.items()
    ]
    await bot.set_my_commands(main_menu_commands)
