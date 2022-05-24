from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from bs4 import BeautifulSoup
        
import requests
import random
import httpx


from config import TOKEN
import userkeyboard as kb

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

'''USERSIDED CLASSES'''
##Minigames
class Games:
    @staticmethod
    def rpc(players_item):
        items = ['rock', 'paper', 'scissors']
        if players_item not in items:
            return 'Wrong item. You can pick only: Rock, Paper or Scissors'

        bots_item = items[random.randint(0, 2)]

        if bots_item == players_item:
            return 'Tie, both of you picked {}'.format(bots_item)

        if (bots_item == 'rock' and players_item == 'scissors') \
                or (bots_item == 'scissors' and players_item == 'paper')\
                or (bots_item == 'paper' and players_item == 'rock'):
            return 'You lost, bot picked {}'.format(bots_item)
        else:
            return 'You won, bot picked {}'.format(bots_item)
##weather
class Tools:
    @staticmethod
    def get_weather(city):
        if not city:
            return 'Specify the city'

        query = ''
        for i in city:
            query += '{}+'.format(i)

        redirect = httpx.get('https://google.com/search?q=погода {}'.format(query))
        document = httpx.get(redirect.headers['location']).text
        soup = BeautifulSoup(document, 'html.parser')
        try:
            temperature = soup.find_all("div", {"class": "BNeawe iBp4i AP7Wnd"})[0].text
        except IndexError:
            return 'Wrong city name'
        return "It is {} in {}".format(temperature, ' '.join(city))

##messaging##

##group msg
'''@dp.message_handler(commands=['start', 'help'])
async def process_commands(message: types.Message):
    try:
        await message.answer("Привет!\nЧто тебе нужно?")
        await message.delete()
    except: 
        await message.reply("открой лс с ботом @uwudateclubot")'''

##echo
'''@dp.message_handler()
async def echo_message(msg: types.Message):
    #await bot.send_message(msg.from_user.id, msg.text)
    await msg.answer(msg.text)
'''

##main commands
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hello, dear User, use /help for further activities")


##button activity
@dp.message_handler(commands=['sharedata'])
async def process_sharedata_command(message: types.Message):
    await message.reply("Tell the bot more about yourself", reply_markup=kb.markup_request)


##inline
@dp.message_handler(commands=['help'])
async def process_command_1(message: types.Message):
    await message.answer("Choose an option", reply_markup=kb.inline_kb_full)

@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.message.delete()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Sofia Shumakova Korovkina\n@zankokunatenshi\n2022')
    

##inline addon handler
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn2'))
async def process_callback_game(callback_query: types.CallbackQuery):
    await callback_query.message.delete()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'To start a game type /rps [rock\scissors\paper]')

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn3'))
async def process_callback_game(callback_query: types.CallbackQuery):
    await callback_query.message.delete()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'To check current weather use /weather [region]')

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn4'))
async def process_callback_game(callback_query: types.CallbackQuery):
    await callback_query.message.delete()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'To provide us with ur contact info use /sharedata')


##add-on handlers
@dp.message_handler(commands=['rps'])
async def rps_handler(message: types.Message):
    await message.reply(Games.rpc(message.get_args().lower()))

@dp.message_handler(commands=['weather'])
async def weather_handler(message: types.Message):
    await message.reply(Tools.get_weather(message.get_args().split()))


#dispatcher exec
if __name__ == '__main__':
    executor.start_polling(dp)
