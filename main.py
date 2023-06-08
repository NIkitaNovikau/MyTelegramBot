from aiogram.utils import executor
from create_bot import dp
from handlers import client
from handlers.client import start_commаnd
from aiogram import types
from sqlite import sql
from UserInformation import user
# import keep_alive


async def on_startup(_):
    await sql.db_start()
    await start_commаnd(types.Message())
    print("Accept")

user.create_profile(dp)
client.register_handlers_client(dp)

# для веб-приложения на лок сервере
# keep_alive.keep_alive()
if __name__ == "__main__":
    executor.start(dp, on_startup(dp))
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)
