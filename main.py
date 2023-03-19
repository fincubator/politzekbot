
#Import modules for functions
import logging

#Import diffrent custom modules 
import config
import languageRU
import languageEN
import languagePL
import languageBY

#Import modules for Aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types.message import ContentType
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, WebAppInfo, InlineKeyboardMarkup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text



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


# b1_RU = KeyboardButton(languageRU.bt_1_kw_1)
# b2_RU = KeyboardButton(languageRU.bt_2_kw_1)
# b3_RU = KeyboardButton(languageRU.bt_3_kw_1)
# b4_RU = KeyboardButton(languageRU.bt_4_kw_1)
# language_keybord = ReplyKeyboardMarkup(resize_keyboard=True) #one_time_keyboard=True чтоб прятать клавиатуру
# language_keybord.add(b1_RU).insert(b2_RU).add(b3_RU).insert(b4_RU)


#choose currency keyboard
b1_RU = KeyboardButton(languageRU.bt_1_kw_wal)
b2_RU = KeyboardButton(languageRU.bt_2_kw_wal)
b3_RU = KeyboardButton(languageRU.bt_3_kw_wal)
b4_RU = KeyboardButton(languageRU.bt_4_kw_wal)
currency_keybord = ReplyKeyboardMarkup(resize_keyboard=True) #one_time_keyboard=True чтоб прятать клавиатуру
currency_keybord.add(b1_RU).insert(b2_RU).add(b4_RU).insert(b3_RU)


#choose currency keyboard
b1_RU = KeyboardButton(languageRU.bt_1_kw_wal_EU)
b2_RU = KeyboardButton(languageRU.bt_2_kw_wal_EU)
b3_RU = KeyboardButton(languageRU.bt_3_kw_wal_EU)
b4_RU = KeyboardButton(languageRU.bt_4_kw_wal_EU)
currency_keybord_EU = ReplyKeyboardMarkup(resize_keyboard=True) #one_time_keyboard=True чтоб прятать клавиатуру
currency_keybord_EU.add(b1_RU).insert(b2_RU).add(b4_RU).insert(b3_RU)


#choose currency keyboard
b1_RU = KeyboardButton(languageRU.bt_1_kw_wal_US)
b2_RU = KeyboardButton(languageRU.bt_2_kw_wal_US)
b3_RU = KeyboardButton(languageRU.bt_3_kw_wal_US)
b4_RU = KeyboardButton(languageRU.bt_4_kw_wal_US)
currency_keybord_US = ReplyKeyboardMarkup(resize_keyboard=True) #one_time_keyboard=True чтоб прятать клавиатуру
currency_keybord_US.add(b1_RU).insert(b2_RU).add(b4_RU).insert(b3_RU)


#choose currency keyboard
b1_RU = KeyboardButton(languageRU.bt_1_kw_wal_PL)
b2_RU = KeyboardButton(languageRU.bt_2_kw_wal_PL)
b3_RU = KeyboardButton(languageRU.bt_3_kw_wal_PL)
b4_RU = KeyboardButton(languageRU.bt_4_kw_wal_PL)
currency_keybord_PL = ReplyKeyboardMarkup(resize_keyboard=True) #one_time_keyboard=True чтоб прятать клавиатуру
currency_keybord_PL.add(b1_RU).insert(b2_RU).add(b4_RU).insert(b3_RU)

#go back keyboard
b1_RU = KeyboardButton(languageRU.bt_4_kw_wal)
currency_keybord_back = ReplyKeyboardMarkup(resize_keyboard=True) #one_time_keyboard=True чтоб прятать клавиатуру
currency_keybord_back.add(b1_RU)



########################### Bot commands ################################
### Work with commands

# @dp.message_handler(commands=['start', 'help'])
# async def command_start(message : types.Message):
#     Politzek_button = InlineKeyboardButton(text='Politzek.me', web_app=WebAppInfo(url='https://belsat.eu/ru'))
#     # keyboard = InlineKeyboardButton(text='chuj', callback_data='like')
#     politzek_web = InlineKeyboardMarkup(row_width=1)
#     politzek_web.add(Politzek_button)
#     # keje.add(keyboard)
#     await bot.send_message(message.from_user.id, languageRU.StartPhrases, reply_markup = politzek_web, parse_mode="Markdown") 
#     # await bot.send_message(message.from_user.id, languageRU.StartPhrases, reply_markup = language_keybord, parse_mode="Markdown") 


# @dp.message_handler(commands=['start', 'help'])
# async def command_start(message : types.Message):
#     Politzek_button = InlineKeyboardButton(text='Politzek.me', web_app=WebAppInfo(url='https://belsat.eu/ru'))
#     # keyboard = InlineKeyboardButton(text='chuj', callback_data='like')
#     politzek_web = InlineKeyboardMarkup(row_width=1)
#     politzek_web.add(Politzek_button)
#     # keje.add(keyboard)
#     await bot.send_message(message.from_user.id, languageRU.StartPhrases, reply_markup = politzek_web, parse_mode="Markdown") 
#     # await bot.send_message(message.from_user.id, languageRU.StartPhrases, reply_markup = language_keybord, parse_mode="Markdown") 


@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, languageRU.give_us_money, reply_markup = currency_keybord, parse_mode="Markdown") 



##Currency logic
#Go back
@dp.message_handler(Text(equals=languageRU.bt_4_kw_wal, ignore_case=True))
async def lests_go(message : types.Message):
    await bot.send_message(message.from_user.id, languageRU.go_back_to_main_menu, reply_markup=currency_keybord, parse_mode="Markdown")

#Go back
@dp.message_handler(Text(equals=languageRU.bt_4_kw_wal_EU, ignore_case=True))
async def lests_go(message : types.Message):
    await bot.send_message(message.from_user.id, languageRU.go_back_to_main_menu, reply_markup=currency_keybord, parse_mode="Markdown")

#EU
@dp.message_handler(Text(equals=languageRU.bt_1_kw_wal, ignore_case=True))
async def lests_go(message : types.Message):
    await bot.send_message(message.from_user.id, languageRU.how_much_money, reply_markup=currency_keybord_EU, parse_mode="Markdown")

#US
@dp.message_handler(Text(equals=languageRU.bt_2_kw_wal, ignore_case=True))
async def lests_go(message : types.Message):
    await bot.send_message(message.from_user.id, languageRU.how_much_money, reply_markup=currency_keybord_US, parse_mode="Markdown")

#PL
@dp.message_handler(Text(equals=languageRU.bt_3_kw_wal, ignore_case=True))
async def lests_go(message : types.Message):
    await bot.send_message(message.from_user.id, languageRU.how_much_money, reply_markup=currency_keybord_PL, parse_mode="Markdown")






########################################## Payment invoice ########################################

@dp.message_handler(Text(equals=languageRU.bt_1_kw_wal_EU, ignore_case=True), state='*' )
@dp.message_handler(Text(equals=languageRU.bt_2_kw_wal_EU, ignore_case=True), state='*' )
@dp.message_handler(Text(equals=languageRU.bt_3_kw_wal_EU, ignore_case=True), state='*' )
@dp.message_handler(Text(equals=languageRU.bt_1_kw_wal_US, ignore_case=True), state='*' )
@dp.message_handler(Text(equals=languageRU.bt_2_kw_wal_US, ignore_case=True), state='*' )
@dp.message_handler(Text(equals=languageRU.bt_3_kw_wal_US, ignore_case=True), state='*' )
@dp.message_handler(Text(equals=languageRU.bt_1_kw_wal_PL, ignore_case=True), state='*' )
@dp.message_handler(Text(equals=languageRU.bt_2_kw_wal_PL, ignore_case=True), state='*' )
@dp.message_handler(Text(equals=languageRU.bt_3_kw_wal_PL, ignore_case=True), state='*' )
async def buy(message: types.Message, state: FSMContext):
    PAYMENT_TOKEN = ''
    if config.PAYMENTS_TOKEN_STRIPE_TEST.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id, languageRU.info_for_users, reply_markup=currency_keybord_back, parse_mode="Markdown")
        PAYMENT_TOKEN = config.PAYMENTS_TOKEN_STRIPE_TEST
    
    #Define image
    PHOTO_URL = 'https://focus.ua/static/storage/originals/8/52/65cda35bcf74cf80f0f0384bdf483528.jpg'
    MESSAGE_PAYMENT = 'Для политзаключенных 🤍❤️🤍'

    #Wybór waluty
    if message.text == languageRU.bt_1_kw_wal_EU: 
        CURRENCY = languageRU.currency_EU
        PRICE = types.LabeledPrice(label=MESSAGE_PAYMENT, amount=1000)
    elif message.text == languageRU.bt_2_kw_wal_EU: 
        CURRENCY = languageRU.currency_EU
        PRICE = types.LabeledPrice(label=MESSAGE_PAYMENT, amount=5000)
    elif message.text == languageRU.bt_3_kw_wal_EU: 
        CURRENCY = languageRU.currency_EU
        PRICE = types.LabeledPrice(label=MESSAGE_PAYMENT, amount=10000)
    elif message.text == languageRU.bt_1_kw_wal_US: 
        CURRENCY = languageRU.currency_US
        PRICE = types.LabeledPrice(label=MESSAGE_PAYMENT, amount=1000)
    elif message.text == languageRU.bt_2_kw_wal_US: 
        CURRENCY = languageRU.currency_US
        PRICE = types.LabeledPrice(label=MESSAGE_PAYMENT, amount=5000)
    elif message.text == languageRU.bt_3_kw_wal_US: 
        CURRENCY = languageRU.currency_US
        PRICE = types.LabeledPrice(label=MESSAGE_PAYMENT, amount=10000)
    elif message.text == languageRU.bt_1_kw_wal_PL: 
        CURRENCY = languageRU.currency_PL
        PRICE = types.LabeledPrice(label=MESSAGE_PAYMENT, amount=1000)
    elif message.text == languageRU.bt_2_kw_wal_PL: 
        CURRENCY = languageRU.currency_PL
        PRICE = types.LabeledPrice(label=MESSAGE_PAYMENT, amount=5000)
    elif message.text == languageRU.bt_3_kw_wal_PL: 
        CURRENCY = languageRU.currency_PL
        PRICE = types.LabeledPrice(label=MESSAGE_PAYMENT, amount=10000)

    await bot.send_invoice(message.chat.id,
                            title= MESSAGE_PAYMENT, 
                            description= MESSAGE_PAYMENT,
                            provider_token=PAYMENT_TOKEN,
                            currency = CURRENCY,
                            photo_url= PHOTO_URL,
                            photo_width=512,
                            photo_height=512,
                            photo_size=512,
                            is_flexible=False,
                            prices=[PRICE],
                            start_parameter='denejki',
                            payload='text_invoice_payload')


#pre checkout
@dp.pre_checkout_query_handler(lambda query: True)
async def pre_chekout_query(pre_chekout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_chekout_q.id, ok=True)


#successful payment
@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message, state: FSMContext):
    print('SUCCESSFUL PAYMENT: ')
    payment_info = message.successful_payment.to_python()
    for k,v in payment_info.items():
        print(f"{k} = {v}")








###################################################### Start bot ##################################################

#run long polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)


