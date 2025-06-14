def create_table (table_name, columns):
    sql_create_table =  f"CREATE TABLE {table_name} ({columns})"
    return sql_create_table
    pass

def insert_data(table_name, line, data_name):
    data_insert = f"INSERT INTO {table_name} ({line}) VALUES ({data_name});"
    return data_insert
pass    


# def check_user(user_name, user_passwd):
#     query = f"SELECT * FROM user WHERE user_name = '{user_name}' AND user_passwd = '{user_passwd}'  "
#     curseur.execute(query,(user_name, user_passwd))
#     result = curseur.fetchone()
#     return result
    # print(f'Welcome back {user_name}' if result else "You don't have an account. Please sign-in.")