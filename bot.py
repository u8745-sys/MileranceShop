import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.telegram import TelegramAPIServer
from config import BOT_TOKEN
from database import init_db
from handlers import router
from admin import router as admin_router

API_SERVER = TelegramAPIServer.from_base("https://tg-bot-api.lol")

async def main():
    init_db()
    bot = Bot(token=BOT_TOKEN, base=API_SERVER)
    dp = Dispatcher()
    dp.include_router(router)
    dp.include_router(admin_router)
    print("✅ Бот запущен через зеркало!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())