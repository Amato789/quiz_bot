import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from core.config import TOKEN, ADMIN_ID
from core.handlers import basic
from core.handlers import registration
from core.handlers import quiz
from core.utils.reg_steps import StepsReg
from core.utils.commands import set_commands


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(ADMIN_ID, text="Bot started!")


async def stop_bot(bot: Bot):
    await bot.send_message(ADMIN_ID, text="Bot stopped!")


async def start():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(name)s - "
               "(%(filename)s).%(funcName)s%(lineno)d - %(message)s"
    )
    bot = Bot(token=TOKEN, parse_mode='HTML')
    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(basic.get_start, Command(commands='start'))

    dp.callback_query.register(quiz.question_1, lambda x: x.data == 'pass_test')
    dp.poll_answer.register(quiz.get_answer)

    dp.callback_query.register(registration.get_fio, lambda x: x.data == 'registration')
    dp.message.register(registration.get_phone, StepsReg.get_fio)
    dp.message.register(registration.get_email, StepsReg.get_phone)
    dp.message.register(registration.get_result, StepsReg.get_email)


    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
