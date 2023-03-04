from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from parser import get_horoscope

bot = Bot(token=TOKEN)  # Token is not provided into github-version of this project, since I don't really want my bot to become public property
dp = Dispatcher(bot=bot)
zodiac_signs = ['овен', 'телец', 'близнецы', 'рак', 'лев', 'дева', 'весы', 'скорпион', 'стрелец', 'козерог', 'водолей', 'рыбы']


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer('Привет. Напиши свой знак зодиака и получишь гороскоп на сегодня. Всё просто:)\nЧто-то не получается? Напиши "/help"')


@dp.message_handler(commands=['help'])
async def start_handler(message: types.Message):
    await message.answer('Бот принимает на вход одно слово - знак зодиака (в именительном падеже и единственном числе), а затем отправляет сегодняшний гороскоп соответствующего знака.\nСуществующие знаки зодиака: овен, телец, близнецы, рак, лев, дева, весы, скорпион, стрелец, козерог, водолей, рыбы. Регистр не имеет значения.')


@dp.message_handler()
async def text_handler(message: types.Message):
    if message.text.strip().lower() in zodiac_signs:
        horoscope = get_horoscope(message.text.strip().lower())
        await message.reply(horoscope)
    else:
        await message.reply(f'{message.text} - это вообще знак зодиака? Не могу найти подходящий гороскоп... Напиши "/help", чтобы узнать больше о работе бота.')


if __name__ == '__main__':
    executor.start_polling(dp)
