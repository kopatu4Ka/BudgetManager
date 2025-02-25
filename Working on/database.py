import sqlite3

def add_transaction(amount, category, type_, date):
    conn = sqlite3.connect("finance.db")  # Подключаемся к БД
    cursor = conn.cursor()

    cursor.execute("INSERT INTO transactions (amount, category, type, date) VALUES (?, ?, ?, ?)",
               (amount, category, type_, date))

    conn.commit()  # Сохранение изменений
    conn.close()  # Закрытие соединения

def delete_transaction(transaction_id):
    conn = sqlite3.connect("finance.db")  # Подключаемся к БД
    cursor = conn.cursor()

    cursor.execute("DELETE FROM transactions WHERE id = ?", transaction_id)

    conn.commit()  # Сохранение изменений
    conn.close()  # Закрытие соединения

def clear_db():
    conn = sqlite3.connect("finance.db")  # Подключаемся к БД
    cursor = conn.cursor()

    cursor.execute("DELETE FROM transactions")
    conn.commit()  # Сохранение изменений

    cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'transactions'")
    conn.commit()  # Сохранение изменений
    conn.close()  # Закрытие соединения

def get_transactions():
    conn = sqlite3.connect("finance.db")  # Подключаемся к БД
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions")  # Запрос всех данных
    rows = cursor.fetchall()  # Получение всех строк

    for row in rows:
        print(row)  # Вывод каждой строки

    conn.close()  # Закрытие соединения

def create_db():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        type TEXT CHECK(type IN ('income','expense')) NOT NULL,
        date TEXT NOT NULL
    )
    """)

    conn.commit()  # Сохранение изменений
    conn.close()  # Закрытие соединения

create_db()