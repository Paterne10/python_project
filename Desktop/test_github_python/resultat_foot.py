liste_game = []

def get_user_input(output):
        a = input(output)
        return a
    
a = get_user_input('What is your name ?')

def get_numeric_value(a):
    while True:
        if a == '':
            print('Input cannot be empty')
            continue
        try:
            a_int = int(a)
            if a_int >= 0:
                return a_int
            else:
                print('Avoid negative number. Try again')
        except ValueError:
            print('You have to enter a number. Try again.')

number_game = get_numeric_value('How many game do you want to register ? ')

for i in range(number_game):
    # Gérer plus de cas d'erreur comme l'entrée de symboles, de chiffres etc....(Créer une fonction)
    while True:
        opponent_name = input(f'What is the name of the opponent team n°{i+1} ? ')
        if opponent_name == '':
            print('Input cannot be empty. Enter the name of the team that you play against.')
            continue

        if not any(char.isalnum() for char in opponent_name):
            print('Enter a valide team name. Avoid symbols and characters.')
            continue
        break

    goal_scored = get_numeric_value('How many goals did you score ? ')
    goal_concede = get_numeric_value('How many goal did you concede ? ')

    # dictionnary data
    dictionnary_game = {'name': opponent_name, 'goal_score':goal_scored, 'goal_concede': goal_concede}

    # Ajout du dictionnaire dans la liste.
    liste_game.append(dictionnary_game)
    print()

print()

print('Total game:', len(liste_game))

# nombre de victoire
print('Number of win:', len([n for n in liste_game if n['goal_score'] > n['goal_concede']]), 'win') 

# nombre de défaite.
print('Number of lose:', len([n for n in liste_game if n['goal_score'] < n['goal_concede']]), 'lose') 

# nombre de match nul.
print('Number of draw:', len([n for n in liste_game if n['goal_score'] == n['goal_concede']]), 'draw') 

# Total de buts marqués.
print('Total goals scored:',sum([n['goal_score'] for n in liste_game]), 'goals')

# Match avec la plus large victoire.
# print('Biggest victory:', max([n for n in liste_game if n['goal_score'] > n['goal_concede']]))
