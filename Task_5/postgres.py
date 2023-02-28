import psycopg2


# Функция создания базы данных
def create_base(conn):
    with conn.cursor() as cur:
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
        conn.commit()


# Функция добавления клиента
def add_client(conn):
    name, surname = input("Введите (через пробел) имя и фамилию ").split(" ")
    email = input("Введите адрес электронной почты ")
    phone = tuple(input("Введите номера телефонов(через пробел) ").split(" "))
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO customer_db(name, surname, email) values(%s, %s, %s) returning client_id;
        """,
            (name, surname, email),
        )
        cust_id = cur.fetchone()[0]
        conn.commit()
        for i in phone:
            cur.execute(
                """
            INSERT INTO phone_db(phone_id, phone_number) values(%s, %s);
            """,
                (cust_id, i),
            )
        conn.commit()


# Функция добавления номера телефонов
def add_phone(conn):  # Можно довавить отбивку что такой номер уже есть
    client_id = int(input("Введите id клиента "))
    phone = input("Введите номер телефона ")
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO phone_db(phone_id, phone_number) values(%s, %s);
        """,
            (client_id, phone),
        )
        conn.commit()


# Функция изменения
def make_changes(conn):
    client_id = int(input("Введите id клиента "))
    print("Если хотите изменить Фамилию , введите 1 ")
    print("Если хотите изменить Имя , введите 2 ")
    print("Если хотите изменить email , введите 3 ")
    print("Если хотите изменить телефон , введите 4 ")
    options = input("Введите действие: ")
    with conn.cursor() as cur:
        if options == "1":
            new_surname = input("Введите новую фамилию ")
            cur.execute(
                """
                        UPDATE customer_db SET surname=%s WHERE client_id=%s;
                        """,
                (new_surname, client_id),
            )
        if options == "2":
            new_name = input("Введите новое Имя ")
            cur.execute(
                """
                        UPDATE customer_db SET name=%s WHERE client_id=%s;
                        """,
                (new_name, client_id),
            )
        if options == "3":
            new_email = input("Введите новый email ")
            cur.execute(
                """
                        UPDATE customer_db SET email=%s WHERE client_id=%s;
                        """,
                (new_email, client_id),
            )
        if options == "4":
            new_phone = input("Введите новый телефон ")
            cur.execute(
                """
                        UPDATE phone_db SET phone_number=%s WHERE phone_id=%s;
                        """,
                (new_phone, client_id),
            )
        conn.commit()


# Функция удаления номера телефонов
def delete_phone(conn):
    client_id = int(input("Введите id клиента "))

    with conn.cursor() as cur:
        cur.execute(
            """
        DELETE FROM phone_db WHERE phone_id=%s;
        """,
            (client_id,),
        )
        conn.commit()


# Функция удаления номера телефонов
def delete_client(conn):
    client_id = int(input("Введите id клиента "))
    with conn.cursor() as cur:
        cur.execute(
            """
        DELETE FROM customer_db WHERE client_id=%s;
        """,
            (client_id,),
        )
        conn.commit()


# Функция для поиска клиента
def find_client(conn):
    find_word = input(
        "Введите данные для поиска клиента \n Имя или Фамилию или номер телефона или email :"
    )
    with conn.cursor() as cur:
        cur.execute(
            """
                    SELECT * FROM customer_db c
                    LEFT JOIN phone_db p ON c.client_id = p.phone_id
                    WHERE  name=%s OR surname=%s OR email=%s or phone_number=%s;
                    """,
            (find_word, find_word, find_word, find_word),
        )
        result = cur.fetchall()
        print(result)
    # return result


conn = psycopg2.connect(
    database="netology_db", user="postgres", password="Мой", host="localhost"
)

# a = create_base(conn)  # Функция создания базы данных
# b = add_client(conn)  # Функция добавления клиента
# c = add_phone(conn)       # Функция добавления номера телефонов
# d = delete_phone(conn)   # Функция удаления номера телефонов
# i = find_client(conn)  # Функция для поиска клиента
# f = make_changes(conn)  # Функция изменения

conn.close()
