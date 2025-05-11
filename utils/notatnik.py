users=[
    {"name":"Antek","location":"Zwoleń","posts":500},
]
def update_user(users_data: list)->None:

    uzytkownik_do_edycji = input('podaj użytkownika do edycji: ')
    for user in users_data:
        if user['name'] == uzytkownik_do_edycji:
            user['name']=input('podaj nowe imie uzytkownika: ')
            user['location']=input('podaj nową lokalizacje uzytkownika: ')
            user['posts']=int(input('podaj nową liczbe postów: '))


update_user(users)

print(users)
