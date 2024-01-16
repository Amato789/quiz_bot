from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Пройти тест', callback_data='pass_test')
    keyboard_builder.button(text='Форма регистрации', callback_data='registration')
    keyboard_builder.adjust(1, 1)
    return keyboard_builder.as_markup()


def get_inline_registration():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Форма регистрации', callback_data='registration')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()
