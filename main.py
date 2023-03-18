
#Import modules for functions
import logging

#Import diffrent custom modules 
import toml
import languageRU
import languageEN
import languagePL
import languageBY

#Import modules for Aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types.message import ContentType
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text


with open('secrets.toml') as f:
    key=toml.parse(f.read())


########################### Bot configruration ################################
### Standart things for work
#log
logging.basicConfig(level=logging.INFO)

#definicja pamięci
starage = MemoryStorage()

#init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=starage)




###################################################### Keyboards configruration ##################################################









########################### Bot commands ################################
### Work with commands

@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, languageRU.RuFirstFraze, parse_mode="Markdown") 












###################################################### Start bot ##################################################

#run long polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)


