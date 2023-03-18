# Import modules for functions
import logging
import asyncio
import toml

# Import diffrent custom modules
import languageRU as RU
import languageEN
import languagePL
import languageBY

# Import modules for Aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

with open('secrets.toml') as f:
    key = toml.loads(f.read())["key"]

########################### Bot configruration ################################
### Standart things for work
# log
logging.basicConfig(level=logging.INFO)

dp = Dispatcher()

# init
bot = Bot(token=key)
dp = Dispatcher()


###################################################### Keyboards configruration ##################################################

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(RU.RuStartPhrases)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


########################### Bot commands ################################
### Work with commands

@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, RU.RuFirstFraze, parse_mode="Markdown")


###################################################### Start bot ##################################################

# run long polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
