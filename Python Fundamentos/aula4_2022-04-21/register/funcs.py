import uuid

def save_user(name, birth_date, csv_file):
    user_id = str(uuid.uuid4())

    #writerow() recebe uma lista contendo os valores que serão
    #escritos no arquivo .csv
    csv_file.writerow([user_id, birth_date, name])

    #writerows() recebe uma lista de listas, sendo essas listas
    #preenchidas com os valores que serão inseridos no arquivo.
    """
    csv_file.writerows(
        [
        [str(uuid.uuid4()), "viviane", "20000409"],
       [str(uuid.uuid4()), "julia", "20020519"],
        [str(uuid.uuid4()), "nicolas", "20000506"]
    ])
    """

def list_users(csv_file):
    for user in csv_file:
        print(user)
