import aiosqlite

from config import DB_NAME


async def init_db():
    """
    Создает таблицу weather_history при запуске сервера, если её ещё нет
    """

    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS weather_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT NOT NULL,
                temperature REAL,
                description TEXT,
                wind_speed REAL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        await db.commit()


async def save_weather_to_db(
    city: str,
    temp: float,
    description: str,
    wind: float
):
    """
    Сохраняет новую запись о погоде в таблицу weather_history.
    TODO для учеников:
    1. Откройте соединение с DB_NAME через async with aiosqlite.connect(...)
    2. Выполните SQL-запрос:
       INSERT INTO weather_history (city, temperature, description, wind_speed) VALUES (?, ?, ?, ?)
    3. Сохраните изменения: await db.commit()
    """

    pass


async def get_weather_history() -> list:
    """
    Возвращает всю историю запросов погоды из БД (от новых к старым).
    TODO для учеников:
    1. Откройте соединение с базой данных.
    2. Выполните запрос:
       SELECT id, city, temperature, description, wind_speed, created_at
       FROM weather_history ORDER BY id DESC
    3. Получите все строки через await cursor.fetchall()
    4. Преобразуйте строки в список словарей с ключами:
       id, city, temperature, description, wind_speed, created_at
    """

    return []


async def delete_city_history(city: str) -> int:
    """
    Удаляет все записи для указанного города и возвращает количество удаленных строк.
    TODO для учеников:
    1. Откройте соединение с базой данных.
    2. Выполните запрос:
       DELETE FROM weather_history WHERE LOWER(city) = LOWER(?)
    3. Сохраните изменения (commit).
    4. Верните cursor.rowcount
    """

    return 0
