from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from create_bot import bot
from keyboard import keyboards

from sqlite import sql


class ProfileStatesGroup(StatesGroup):

    photo = State()
    name = State()
    age = State()
    description = State()


async def cmd_cancel(message: types.Message, state: FSMContext):
    if state is None:
        return

    await state.finish()
    await message.reply('Вы прервали создание анкеты!',
                        reply_markup=keyboards.get_create_kb())


async def cmd_start(message: types.Message) -> None:
    await message.answer('Вы решили начать создавать профиль? Тогда введите - /createProfile',
                         reply_markup=keyboards.get_create_kb())

    await sql.create_profile(user_id=message.from_user.id)


async def cmd_create(message: types.Message) -> None:
    await message.reply("Давайте начнем создавать ваш профиль, для начала отправьте мне свою фотографию пожалуйста!",
                        reply_markup=keyboards.get_cancel_kb())
    await ProfileStatesGroup.photo.set()  # установили состояние фото


async def check_photo(message: types.Message):
    await message.reply('Это не фотография!')


async def load_photo(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id

    await message.reply('Теперь отправь своё имя!')
    await ProfileStatesGroup.next()


async def check_age(message: types.Message):
    await message.reply('Введите реальный возраст!')


async def load_name(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['name'] = message.text

    await message.reply('Сколько тебе лет?')
    await ProfileStatesGroup.next()


async def load_age(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['age'] = message.text

    await message.reply('А теперь расскажи немного о себе!')
    await ProfileStatesGroup.next()


async def load_desc(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['description'] = message.text
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=data['photo'],
                             caption=f"{data['name']}, {data['age']}\n{data['description']}")

    await sql.edit_profile(state, user_id=message.from_user.id)
    await message.reply('Ваша акнета успешно создана!')
    await state.finish()


def create_profile(dp: Dispatcher):
    dp.register_message_handler(cmd_cancel, commands=['cancelProfile'], state='*')
    dp.register_message_handler(cmd_start, commands=['startProfile'])
    dp.register_message_handler(cmd_create, commands=['createProfile'])
    dp.register_message_handler(check_photo, lambda message: not message.photo, state=ProfileStatesGroup.photo)
    dp.register_message_handler(load_photo, content_types=['photo'], state=ProfileStatesGroup.photo)
    dp.register_message_handler(check_age, lambda message: not message.text.isdigit() or float(message.text) > 100,
                        state=ProfileStatesGroup.age)
    dp.register_message_handler(load_name, state=ProfileStatesGroup.name)
    dp.register_message_handler(load_age, state=ProfileStatesGroup.age)
    dp.register_message_handler(load_desc, state=ProfileStatesGroup.description)