import os.path
import json
filename = 'database_compte_p_money.py'
def create_file (filename):
    f = open( filename, 'w')
    f.write('#fichier cree avec succes')
    f.close()
    pass

def read_file(filename):
    f = open(filename, 'r')
    contenu = f.read()
    f.close()
    return contenu

create_file(filename)

# data = {'Nom': 'John Doe', 'Age': 30, 'Amis': ['Ghost', 'Apha']}

# file_name = 'stage.txt'
# json_file = json.dumps(data)

# print(json_file)

# f = open('stage.txt', 'w')
# f.write(json_file)
# f.close()
# f = open(file_name, 'r')
# datas = f.read()
# f.close()

# person = json.loads(datas)

# print(f'Nom: {person['Nom']}')
