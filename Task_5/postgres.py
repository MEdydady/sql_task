import psycopg2


# Функция создания базы данных
def create_base(cur):
    cur.execute(
        """
                DROP TABLE IF EXISTS phone_db;
                DROP TABLE IF EXISTS customer_db;
                CREATE TABLE customer_db(
                    client_id SERIAL PRIMARY KEY,
                    name  VARCHAR(255) NOT NULL,
                    surname VARCHAR(255) NOT NULL,
                    email   VARCHAR(255) NOT NULL
                );
                CREATE TABLE phone_db(
                    phone_id integer  references customer_db(client_id),
                    phone_number VARCHAR(255)
                );
        """
    )


# Функция добавления клиента
def add_client(cur, name, surname, email):
    cur.execute(
        """
            INSERT INTO customer_db(name, surname, email) values(%s, %s, %s) returning client_id;
        """,
        (name, surname, email),
    )


# Функция добавления номера телефонов
def add_phone(cur, client_id, phone):  # Можно довавить отбивку что такой номер уже есть
    cur.execute(
        """
            INSERT INTO phone_db(phone_id, phone_number) values(%s, %s);
        """,
        (client_id, phone),
    )


# Функция изменения
def make_changes(cur, client_id, name=None, surname=None, email=None, phone=None):
    if name != None:
        cur.execute(
            """
        UPDATE customer_db SET name=%s WHERE client_id=%s
        """,
            (name, client_id),
        )
    if surname != None:
        cur.execute(
            """
        UPDATE customer_db SET surname=%s WHERE client_id=%s
        """,
            (surname, client_id),
        )
    if email != None:
        cur.execute(
            """
        UPDATE customer_db SET email=%s WHERE client_id=%s
        """,
            (email, client_id),
        )
    if phone != None:
        cur.execute(
            """
        UPDATE phone_db SET phone=%s WHERE client_id=%s
        """,
            (client_id, phone),
        )


# Функция удаления номера телефонов
def delete_phone(cur, phone):
    cur.execute(
        """
        DELETE FROM phone_db WHERE phone_number=%s;
        """,
        [phone],
    )


# Функция удаления номера телефонов
def delete_client(cur, client_id):
    cur.execute(
        """
        DELETE FROM customer_db WHERE client_id=%s;
        """,
        (client_id),
    )


# Функция для поиска клиента
def find_client(cur, name=None, surname=None, email=None, phone=None):
    if name != None:
        cur.execute(
            """
        SELECT cd.name, cd.surname, cd.email, pd.phone_number FROM customer_db cd
        LEFT JOIN phone_db pd ON cd.client_id = pd.phone_id
        WHERE name=%s;
        """,
            [name],
        )
    if surname != None:
        cur.execute(
            """
        SELECT cd.name, cd.surname, cd.email, pd.phone_number FROM customer_db cd
        LEFT JOIN phone_db pd ON cd.client_id = pd.phone_id
        WHERE surname=%s;
        """,
            (surname),
        )
    if email != None:
        cur.execute(
            """
        SELECT cd.name, cd.surname, cd.email, pd.phone_number FROM customer_db cd
        LEFT JOIN phone_db pd ON cd.client_id = pd.phone_id
        WHERE email=%s;
        """,
            (email),
        )
    if phone != None:
        cur.execute(
            """
        SELECT cd.name, cd.surname, cd.email, pd.phone_number FROM customer_db cd
        LEFT JOIN phone_db pd ON cd.client_id = pd.phone_id
        WHERE phone_number=%s;
        """,
            (phone),
        )
    result = cur.fetchall()
    print(result)


if __name__ == "__main__":
    with psycopg2.connect(
        database="netology_db", user="postgres", password="Мой", host="localhost"
    ) as conn:
        with conn.cursor() as cur:
            create_base(cur)
            add_client(cur, "Daniil", "Medvedev", "dan@ya.ru")
            add_client(cur, "Dari", "Sgerbakova", "dar@ya.ru")
            conn.commit()
            add_phone(cur, "1", "212121212")
            add_phone(cur, "1", "2323232323")
            add_phone(cur, "2", "3434343")
            conn.commit()
            make_changes(cur, "1", name="Danilka", surname="Beer")
            make_changes(cur, "1", surname="Medvedka")
            conn.commit()
            find_client(cur, name="Dari")
            conn.commit()
            delete_phone(cur, "3434343")
            delete_client(cur, "2")
            conn.commit()
