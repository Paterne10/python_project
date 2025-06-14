import sqlite3
# Création de la base de données.
database_name = 'user_account'
connection = sqlite3.connect(database_name)

# Fonction pour créer des tables.
def create_table(table_name, data):
    table = f"CREATE TABLE {table_name} ({data})"
    return table

# Fonction pour insérer des données dans la table.
def insert_data (table_name, line, datas):
    data = f"INSERT INTO {table_name} ({line}) VALUES ({datas}) "
    return data

# création des différentes tables.

# user_table = create_table('user', ("use_id INTEGER NOT NULL PRIMARY KEY, user_name VARCHAR, user_first_name VARCHAR, user_passwd VARCHAR"))

# Mise a jour de la table user.
# add_column = "ALTER TABLE user ADD COLUMN email VARCHAR"
curseur = connection.cursor()
# curseur.execute(add_column)

# curseur.execute(user_table)
# Fonction qui affiche le menu d'inscription.
def sign_menu():
    print('Sign in')
    user_name = input('Enter the name: ')
    user_first_name = input('Enter the first name: ')
    user_mail = input('Enter your mail address: ')
    user_passwd = input('Enter the password: ')
    return user_name, user_first_name, user_passwd, user_mail

# Fonction qui affiche le menu d'inscription.
def login_menu():
    print('Login')
    user_name = input('Enter the name: ')

    user_passwd = input('Enter the password: ')
    return user_name, user_passwd

# Fonction qui vérifie l'existence de l'utilisateur.
def check_user(user_name, user_passwd):
    query = f"SELECT * FROM user WHERE user_name = '{user_name}' AND user_passwd = '{user_passwd}'  "
    curseur.execute(query)
    result = curseur.fetchone()
    print(f'Welcome back {user_name}' if result else "You don't have an account. Please sign-in.")

# Programme principale.
print("Welcome to our website")
print('1- Sign in')
print('2- Login')
user_choice = input('Reply: ')

if user_choice == '1':
    user_name, user_first_name, user_passwd, user_mail = sign_menu()
    user = insert_data('user', ('user_name, user_first_name, user_passwd, email'), (f'"{user_name}", "{user_first_name}", "{user_passwd}","{user_mail}"'))
    curseur.execute(user)
    print("Your account has been succesfully registered.")

elif user_choice == '2':
    user_name, user_passwd = login_menu()
    check = check_user(user_name, user_passwd)


# Last point:
    # Ajout des adresses-mail dans la BD


# Menu inscription.
# if user_choice == '1':
#     user_name = input('Enter the name: ')
#     user_first_name = input('Enter the first name: ')
#     user_passwd = input('Enter the password: ')

#     user = insert_data('user', ('user_name, user_first_name, user_passwd'), (f'"{user_name}", "{user_first_name}", "{user_passwd}"'))
#     curseur.execute(user)
#     query = f"SELECT * FROM user WHERE user_name = '{user_name}' AND user_passwd = '{user_passwd}'"
#     curseur.execute(query)
#     result = curseur.fetchone()

# # menu connexion.
# elif user_choice == '2':
#     user_name = input('Enter the name: ')
#     user_passwd = input('Enter the password: ')

#     query = f"SELECT * FROM user WHERE user_name = '{user_name}' AND user_passwd = '{user_passwd}'"
#     curseur.execute(query)
#     result = curseur.fetchone()

#     if result:
#         print(f"Welcome back {user_name}")
#     else:
#         print('You have to sign in.')


# Ajout de plusieurs utilisateurs.
# user_number = int(input('How many user(s) do you want to register: '))

# for i in range(user_number):
#     print(f"user n° {i+1}")
#     user_name = input('Enter the name: ')
#     user_first_name = input('Enter the first name: ')
#     user_passwd = input('Enter the password: ')

#     user = insert_data('user', ('user_name, user_first_name, user_passwd'), (f'"{user_name}", "{user_first_name}", "{user_passwd}"'))

#     curseur.execute(user)
#     print()
# print("The user(s) was succesfully register.") 

connection.commit()
connection.close()