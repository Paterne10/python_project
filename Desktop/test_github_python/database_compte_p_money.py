import sqlite3
import fonction_requete_sql

# database creation.
DATABASE_NAME = 'userAccount'

connection = sqlite3.connect(DATABASE_NAME)
curseur = connection.cursor()

user_table = 'users'
curseur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{user_table}'")

if curseur.fetchone() is None:
    create_user_table = f'''CREATE TABLE { user_table} (
        userID INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name VARCHAR(100),
        user_firstName VARCHAR(100),
        user_birthdate DATE,
        user_mail VARCHAR(150),
    )'''

    curseur.execute(create_user_table)
    connection.commit()

account_table = "accounts"
curseur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{user_table}'")

if curseur.fetchone() is None:

    create_accoun_table = f'''CREATE TABLE {account_table} (
        account_number INTEGER PRIMARY KEY AUTOINCREMENT,
        balance INTEGER,
        creation_date DATE,
        password VARCHAR(255),
        phone_number VARCHAR(20) UNIQUE,
        userID INTEGER,
        FOREIGN KEY (userID) REFERENCES users(userID)
    )'''

    curseur.execute(create_accoun_table)
    connection.commit()
# Last point: Revoir le comportement de cette requete.
