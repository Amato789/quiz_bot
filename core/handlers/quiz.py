from aiogram import Bot, types
from core.utils import db_connection
from core.keyboards.inline import get_inline_registration

my_quiz = None
discount = 10


async def question_1(callback_query: types.CallbackQuery):
    global my_quiz

    my_quiz = await callback_query.message.answer_poll(
        question='1. Какой из перечисленных языков программирования чаще всего используется для веб-разработки?',
        options=['a. Java', 'b. Python', 'c. HTML'],
        type='quiz',
        correct_option_id=2,
        is_anonymous=False,
    )
    await callback_query.answer()


async def get_answer(poll: types.PollAnswer, bot: Bot):
    global my_quiz
    global discount

    if my_quiz.poll.question.startswith('1'):
        if int(poll.option_ids[0]) == int(my_quiz.poll.correct_option_id):
            discount += 5

        my_quiz = await bot.send_poll(
            poll.user.id,
            question='2. Какая из следующих технологий используется для хранения данных?',
            options=['a. XML', 'b. SQL', 'c. CSS'],
            type='quiz',
            correct_option_id=1,
            is_anonymous=False
        )
        db_connection.change_quiz_status(telegram_id=poll.user.id, quiz_status=False, answers=1, discount=discount)

    elif my_quiz.poll.question.startswith('2'):
        if int(poll.option_ids[0]) == int(my_quiz.poll.correct_option_id):
            discount += 5

        my_quiz = await bot.send_poll(
            poll.user.id,
            question='3. Что представляет собой Git??',
            options=['a. Офисный пакет', 'b. Система управления версиями', 'c. Веб-браузер'],
            type='quiz',
            correct_option_id=1,
            is_anonymous=False
        )
        db_connection.change_quiz_status(telegram_id=poll.user.id, quiz_status=False, answers=2, discount=discount)

    else:
        if int(poll.option_ids[0]) == int(my_quiz.poll.correct_option_id):
            discount += 5

        await bot.send_message(
            poll.user.id,
            f'Молодец, твой скидка = {discount} %',
            reply_markup=get_inline_registration()
        )
        db_connection.change_quiz_status(telegram_id=poll.user.id, quiz_status=True, answers=3, discount=discount)
