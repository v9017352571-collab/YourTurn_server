# init_db.py
import os
import sqlite3
from data.db_session import global_init


def main():
    db_file = 'db/test_database.sqlite'

    # Удаляем старую тестовую базу, если она есть, для чистоты эксперимента
    if os.path.exists(db_file):
        os.remove(db_file)
        print(f"Старый файл {db_file} удалён.")

    print("Инициализация базы данных...")
    # Эта функция создаст все таблицы из __all_models.py
    global_init(db_file)
    print("База данных успешно создана!\n")

    # Проверяем, что именно создалось
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
    tables = cursor.fetchall()

    print(f"Всего создано таблиц: {len(tables)}")
    print("Список таблиц:")
    for i, table in enumerate(tables, 1):
        print(f"  {i:2d}. {table[0]}")

    conn.close()
    print("\nПроверка завершена. Файл test_database.sqlite готов к просмотру.")


if __name__ == '__main__':
    main()