import psycopg2

def create_wish_list():
    conn = psycopg2.connect(
        dbname="wish_list",
        user="postgres",
        password="postgres",
        host="127.0.0.1",
        port="5432"
    )
    print("Успешное подключение к базе данных 'wish_list'")
    cursor = conn.cursor()

    # TODO: создай таблицу wishes (если не существует):
    # Поля: id (serial), name (text), message (text)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS wishes (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_wish_list()