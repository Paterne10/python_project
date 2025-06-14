import test_input
import database_compte_p_money
import sqlite3
import datetime

# class who create account.
class Compte:    
    def __init__(self, name, firstName, birthdate, mail, number: int, password, balance:int = 0):
        self.name = name
        self.firstName = firstName
        self.birthdate = birthdate
        self.mail = mail
        self.number = number
        self.password = password
        self.balance = balance
   
        
    
    def create_account(self):
        # Verify if the user already have an account associate to the number that he enter.
        database_compte_p_money.curseur.execute(f'SELECT * FROM accounts WHERE phone_number = ? ', (self.number,))
        if database_compte_p_money.curseur.fetchone() is None:
            insert_user = f'''INSERT INTO users (user_name, user_firstName, user_birthdate, user_mail)
                values ('{self.name}', '{self.firstName}', '{self.birthdate}', '{self.mail}')
            '''
            database_compte_p_money.curseur.execute(insert_user)
            user_id = database_compte_p_money.curseur.lastrowid
            date = datetime.datetime.now()
            inser_account = f'''INSERT INTO accounts 
            (balance, creation_date, password, phone_number,  userID)
            values ({self.balance},'{date.strftime("%d-%m-%Y")}', '{self.password}', '{self.number}', {user_id})
            '''
            database_compte_p_money.connection.execute(inser_account)
            print("Account successfully created.")
        else:
            print("This number is already associated to an account.")

    def connect_account(self):
        verification_query = f'SELECT a.phone_number, a.password FROM accounts a JOIN users u ON u.userID = a.userID WHERE (phone_number = ? AND password = ?)'
        database_compte_p_money.curseur.execute(verification_query, (self.number, self.password ))
        result_verification = database_compte_p_money.curseur.fetchone()
        if result_verification:
            print('status: Active')
            print("Welcome to our mobile service")
        else:
            print("phone or password incorrect.")

    def print_info(self):
        print('name:', self.name)
        print('first name:',self.firstName)
        print('birthdate: ',self.birthdate)
        print('mail: ',self.mail)
        print('password: ',self.password)

# The class who make transaction.
class Transaction(Compte):
     def __init__(self, name, firstName, birthdate, mail, number, password, balance = 0):
         Compte.__init__(self, name, firstName, birthdate, mail, number, password, balance)
     def depot(self):
        montant = input('Enter the amount you want to deposit: ')
        self.balance += int(montant)
        deposit_query =  f'UPDATES accounts SET balance = ? WHERE phone_number = ? '
        database_compte_p_money.curseur.execute(deposit_query, (montant, self.number))

        
# The function who get user information.
def get_user_information():
    # username.
    while True:
        name = input("Enter your name: ").upper()
        error = test_input.validate_name(name)
        if not error:
            # add an icon (checkbox)
            print("name successfully registered.")   
            break
            # add an icon(red cross)
        print(test_input.validate_name(name))
    
    # user_first_name.
    while True:
        firstName = input("Enter your first name: ").title()
        error = test_input.validate_name(firstName)
        if not error:   
            print("first name successfully registered.")
            break
        print(test_input.validate_name(firstName))

    # user_birthdate.
    while True:
        birthdate = input("Enter your birthdate (JJ-MM-AAAA pr JJ/MM/AAAA) : ")
        if not birthdate:
            print("Birthdate cannot be empty.")
            continue
        error = test_input.validate_birthdate(birthdate)
        if not error:
            print("birthdate successfully registered.")
            break
        print(error)
        
    # user_mail_address.
    while True:
        mail = input("Entrez votre adresse e-mail : ")
        if not mail:
            print("mail cannot be empty.")
            continue
        error = test_input.validate_mail_address(mail)
        if not error :
            print("mail address successfully registered.")
            break
        print(error)

    # user_password.
    while True:
        user_password = input("Entrez votre mot de passe : ")
        if not user_password:
            print("Password cannot be empty.")
            continue
        error = test_input.validate_password(user_password)
        if not error:
            print("first name successfully registered.")
            break
        print(error)

    number = input("Enter your phone number: ")

    return name, firstName, birthdate, mail, user_password, number


# Main programm.
name, firstName, birthdate, mail, password, number = get_user_information()
compte_1 = Compte(name, firstName, birthdate, mail,number, password)  

database_compte_p_money.connection.commit()
database_compte_p_money.connection.close()

# Last point:
#   Revoir l'implementation de la classe Compte(composition)
    # Revoir la verification des entrées: numero-telephone, mail.





# def main():
#     name, firstName, birthday, mail, password = saisir_informations()
#     compte = Compte(name, firstName, birthday, mail, password)
#     compte.print_info()

# if __name__ == "__main__":
#     main()