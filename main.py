from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import toml
import logging
import asyncio

import languageRU as RU
import languageEN
import languagePL
import languageBY

with open('secrets.toml') as f:
    key = toml.loads(f.read())["key"]


logging.basicConfig(level=logging.INFO)

bot = Bot(token=key)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="📜 Статистика"),
            types.KeyboardButton(text="🎲 Случайный"),
            types.KeyboardButton(text="🏠 Города"),
            types.KeyboardButton(text="🔍"),
            types.KeyboardButton(text="🏻 Что писать?")

        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer(RU.RuStartPhrases, reply_markup=keyboard)

@dp.message(Command("write"))
async def what_whrite(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="🏘 Домой")

        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )

    await message.answer(RU.RuWhatToWrite, reply_markup=keyboard)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

