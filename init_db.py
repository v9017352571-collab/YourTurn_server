import asyncio
import os
from data.db_session import init_db, engine


async def main():
    db_path = "db/test_database.sqlite"

    # Удаляем старую БД для чистоты теста
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"Старый файл {db_path} удалён.")

    # Создаем папку db, если её нет
    os.makedirs("db", exist_ok=True)

    print("Инициализация асинхронной базы данных...")
    await init_db()
    print("✅ База данных успешно создана!")

    # Проверка количества таблиц
    import sqlite3
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name;")
    tables = cursor.fetchall()
    print(f"\nВсего создано пользовательских таблиц: {len(tables)}")
    for i, table in enumerate(tables, 1):
        print(f"  {i:2d}. {table[0]}")
    conn.close()


if __name__ == '__main__':
    asyncio.run(main())