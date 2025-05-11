users=[
    {"name":"Antek","location":"Zwoleń","posts":500},
]


def remove_user(users_data: list)->None:
    uzytkownik_do_usuniecia=input('podaj użytkownika do usuniecia: ')

    for user in users_data:

        if user['name'] == uzytkownik_do_usuniecia:
            users_data.remove(user)


print(users)