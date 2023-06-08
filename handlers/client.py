from aiogram import types, Dispatcher
from keyboard.keyboards import get_start_vzv, get_start_obl, get_find

HELP_COMMAND = """
<em>
/start -> начать работу с ботом
/help -> список команд
/description -> описание нашего бота
/find ->  Поиск информации о курсанте по параметрам
/yval -> увольнение на этой неделе
/doc... -> получить документы
/docInfo -> Список документов
/startProfile -> начать создание профиля курсанта
/createProfile -> создать профиль курсанта
/cancelProfile -> отмена создания профиля
</em>
"""

FIND_COMMAND = """
<em>Введите 1,2 или 3 в зависимости от вашего выбора: 
1) Поиск по области
2) Получение информации по взводам
3) Поиск по фамилии</em>
"""

DESCRIPTION_COMMAND = """
<em>Здраствуйте уважаемые пользователи, мой бот умеет:
1)Производить поиск личных дел курсантов по нескольким параметрам
2)Выдавать расписание занятий отдельных групп
3)Показывать расход личного состава
4)Показывать список увольняемых 
5)Предоставлять готовые рапорта для вас
6)Предоставлять учет лабораторных работ личного состава</em>
"""


async def help_commаnd(message: types.Message):
    await message.answer(text=HELP_COMMAND,
                         parse_mode="HTML")
    await message.delete()


async def start_commаnd(message: types.Message):
    if message.from_user is not None:
        mess = f'Приветствую, <b><u>{message.from_user.first_name}</u></b>. Чтобы ознакомиться с функциями этого бота нажмите /help.'  # вывод имени пользователя; f - форматированная строка
        await message.answer(mess, parse_mode='html')  # именно в этот чат будем кидать сообщение
        await message.delete()


async def weekend_commаnd(message: types.Message):
  if message.text == '/yval':
      text = 'Вот список всех кураснтов 2 курса ВФ БГУИР убывающие в отпуск/увольнение на этой неделе: '
      await message.answer(text=text, parse_mode='html')
      file1 = open("documents/MyFirstBot.docx", "rb")
      file2 = open("documents/MyFirstBot.docx", "rb")
      await message.reply_document(file1)
      await message.reply_document(file2)
      await message.delete()
  else:
      await message.answer("Я не знаю, что это за файл.", parse_mode='html')


async def description_command(message: types.Message):
    await message.answer(text=DESCRIPTION_COMMAND,
                         parse_mode="HTML")
    await message.delete()


async def find_commаnd(message: types.Message):
    await message.answer(text=FIND_COMMAND,
                         parse_mode="HTML",
                         reply_markup=get_find())
    await message.delete()


async def documents(message: types.Message):
    await message.answer(text="<em>Введите /doc маршрутник или /doc еще_что-то для получения файла</em>",
                         parse_mode="HTML")
    await message.delete()


async def get_doc(message: types.Message):
    if message.text == '/doc маршрутник':
        file1 = open("documents/MyFirstBot.docx", "rb")
        await message.reply_document(file1)
    elif message.text == '/doc еще_что-то':
        file2 = open("documents/MyFirstBot.docx", "rb")
        await message.reply_document(file2)


async def choose(message: types.Message):
    if message.text == 'Поиск по области.':
        await message.answer(text='Введите область : ',
                             reply_markup=get_start_obl())
    elif message.text == 'Получение информации по взводам.':
        await message.answer(text='Введите взвод : ',
                             reply_markup=get_start_vzv())
    elif message.text == 'Поиск по фамилии.':
        await message.answer(text='Введите фамилию : ',
                             reply_markup='...')
    await message.delete()


def register_handlers_client(dp: Dispatcher):

    dp.register_message_handler(help_commаnd, commands=['help'])
    dp.register_message_handler(start_commаnd, commands=['start'])
    dp.register_message_handler(description_command, commands=['description'])
    dp.register_message_handler(find_commаnd, commands=['find'])
    dp.register_message_handler(weekend_commаnd, commands=['yval'])
    dp.register_message_handler(documents, commands=['docInfo'])
    dp.register_message_handler(get_doc, commands=['doc'])
    dp.register_message_handler(choose)

