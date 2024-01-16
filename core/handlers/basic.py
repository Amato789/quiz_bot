from aiogram import Bot, types
from core.keyboards.inline import get_inline_keyboard
from core.utils import db_connection


async def get_start(message: types.Message, bot: Bot):
    await message.answer(f'Привет, {message.from_user.first_name}! '
                         f'Я бот для регистрации и прохождения курсов IT-направления. '
                         f'Пройди опрос и получи персональную скидку!', reply_markup=get_inline_keyboard())
    db_connection.db_create()
    if not db_connection.is_user_exist(telegram_id=message.from_user.id):
        print('user exists')
        db_connection.create_new_user(user=message.from_user.username, telegram_id=message.from_user.id)
