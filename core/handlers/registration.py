from aiogram import Bot, types
from aiogram.fsm.context import FSMContext
from core.utils.reg_steps import StepsReg
from core.keyboards.reply import get_reply_keyboard
from core.utils.db_connection import get_user_discount, update_user


async def get_fio(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer(f'Введите свои Ф.И.О.')
    await state.set_state(StepsReg.get_fio)


async def get_phone(message: types.Message, state: FSMContext):
    await message.answer(f'Ваше имя: {message.text}\r\nВведите свой номер телефона:',
                         reply_markup=get_reply_keyboard())
    await state.update_data(fio=message.text)
    await state.set_state(StepsReg.get_phone)


async def get_email(message: types.Message, state: FSMContext):
    await message.answer(f'Ваш номер телефона: {message.contact.phone_number}\r\nВведите свой email:')
    await state.update_data(phone=message.contact.phone_number)
    await state.set_state(StepsReg.get_email)


async def get_result(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    context_data = await state.get_data()
    fio = context_data.get('fio')
    phone = context_data.get('phone')
    email = context_data.get('email')
    users_data = (f'Твои данные\r\n'
                  f'ФИО: {fio}\r\n'
                  f'Номер телефона: {phone}\r\n'
                  f'Email: {email}\r\n'
                  f'Скидка: {get_user_discount(message.from_user.id)}%')
    await message.answer(users_data)
    update_user(telegram_id=message.from_user.id, fio=fio, email=email, phone=phone)
    await message.answer('Поздравляем! Вы оставили свою заявку на прохождение курсов в школе My IT-Tutor. '
                         'В скором времени, с вами свяжется наш менеджер для уточнения деталей направления и '
                         'языка программирования, который вы бы хотели изучить! До скорой встречи!')
    await state.clear()
