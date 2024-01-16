from aiogram.fsm.state import StatesGroup, State


class StepsReg(StatesGroup):
    get_fio = State()
    get_phone = State()
    get_email = State()
    get_quiz_results = State()
