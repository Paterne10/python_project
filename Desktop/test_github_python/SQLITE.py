import sqlite3

# Création de la BD.
connection = sqlite3.connect("FirstDB")

# Fonction qui crée une table.

def create_table (table, colonnes):
    sql_create_table =  f"CREATE TABLE {table} ({colonnes})"
    return sql_create_table

# Fonction qui insère des données.
def insert_data(table_name, line, data_name):
    data_insert = f"INSERT INTO {table_name} ({line}) VALUES ({data_name});"
    return data_insert

# Création de la table artiste.

sql_create_table_artiste = create_table(
    'artiste', 
    'artiste_id INTEGER NOT NULL PRIMARY KEY, ' \
    'nom VARCHAR')

# création de la table album.
sql_create_table_album = create_table(
    'album', 
    'album_id INTEGER NOT NULL PRIMARY KEY,' 
    'artiste_id REFERENCES artiste(artiste_id),' \
    'Titre VARCHAR,' \
    'annee DATE')


curseur = connection.cursor()

curseur.execute(sql_create_table_artiste) 
curseur.execute(sql_create_table_album)

# insérer le nom des artistes et récupération de l'id.".
insert_titre_album_Damso = insert_data("artiste", "nom", "'Damso'")
curseur.execute(insert_titre_album_Damso)
Damso_id = curseur.lastrowid

insert_titre_album_Booba = insert_data("artiste", "nom", "'Booba'")
curseur.execute(insert_titre_album_Booba)
Booba_id = curseur.lastrowid

# Ajout des titres des albums. (Insertion des données dans la table album)
insert_titre_album_Damso = insert_data("album", "Titre, artiste_id, annee", f"'Ipséité', {Damso_id}, 2018")
curseur.execute(insert_titre_album_Damso) 

insert_titre_album_Booba = insert_data("album", "Titre,  artiste_id, annee", f"'Trone', {Booba_id}, 2017")
curseur.execute(insert_titre_album_Booba) 

# On applique les modifications sur la base de données.
connection.commit()

# On ferme la base de données.
connection.close()


# Ajouter les noms des artistes. (Deuxième methode)
# liste_artiste = ['Damso', 'Booba']
# for artiste in liste_artiste:
#     insert_artist = insert_data('artiste', 'nom', f"'{artiste}'")
#     curseur.execute(insert_artist) 
#     artiste_id = curseur.lastrowid
#     curseur.execute(insert_artist) 
