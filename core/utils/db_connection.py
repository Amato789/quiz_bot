import sqlite3

db_name = 'quiz_bot.db'
table_name = 'users'


def db_create():
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        cursor.execute(f"""
                        CREATE TABLE IF NOT EXISTS {table_name} (
                        id INTEGER PRIMARY KEY,
                        user TEXT,
                        telegram_id INTEGER,
                        fio TEXT,
                        email TEXT,
                        phone TEXT,
                        quiz_status BOOL,
                        answers INTEGER,
                        discount INTEGER
                        )
                        """)
        connection.commit()

    except sqlite3.Error as error:
        print('DB connection error', error)
    except Exception as error:
        print(error, type(error))
    finally:
        cursor.close()
        connection.close()


def create_new_user(user: str, telegram_id: int, fio: str = None, email: str = None, phone: str = None,
                    quiz_status: bool = False, answers: int = 0, discount: int = 10):
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        cursor.execute(
            f'INSERT INTO {table_name} (user, telegram_id, fio, email, phone, quiz_status, answers, discount) '
            f'VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
            (user, telegram_id, fio, email, phone, quiz_status, answers, discount)
        )
        connection.commit()
    except sqlite3.Error as error:
        print('DB connection error', error)
    except Exception as error:
        print(error, type(error))
    finally:
        cursor.close()
        connection.close()


def is_user_exist(telegram_id: int):
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        cursor.execute(
            f'SELECT * FROM {table_name} WHERE telegram_id = ?',
            (telegram_id, )
        )
        user_data = cursor.fetchone()
        if user_data:
            return True
        return False
    except sqlite3.Error as error:
        print('DB connection error', error)
    except Exception as error:
        print(error, type(error))
    finally:
        cursor.close()
        connection.close()


def change_quiz_status(telegram_id: int, quiz_status: bool = False, answers: int = 0, discount: int = 10):
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        cursor.execute(
            f'UPDATE {table_name} SET quiz_status = ?, answers = ?, discount = ? WHERE telegram_id = ?',
            (quiz_status, answers, discount, telegram_id),
        )
        connection.commit()
    except sqlite3.Error as error:
        print('DB connection error', error)
    except Exception as error:
        print(error, type(error))
    finally:
        cursor.close()
        connection.close()


def get_user_discount(telegram_id: int):
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        cursor.execute(
            f'SELECT * FROM {table_name} WHERE telegram_id = ?',
            (telegram_id, )
        )
        user_data = cursor.fetchone()
        return user_data[-1]

    except sqlite3.Error as error:
        print('DB connection error', error)
    except Exception as error:
        print(error, type(error))
    finally:
        cursor.close()
        connection.close()


def update_user(telegram_id: int, fio: str = None, email: str = None, phone: str = None):
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        cursor.execute(
            f'UPDATE {table_name} SET fio = ?, email = ?, phone = ? WHERE telegram_id = ?',
            (fio, email, phone, telegram_id)
        )
        connection.commit()
    except sqlite3.Error as error:
        print('DB connection error', error)
    except Exception as error:
        print(error, type(error))
    finally:
        cursor.close()
        connection.close()
