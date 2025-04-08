users=[
    {"name":"Antek","location":"Zwoleń","posts":500},
    {"name":"Michał","location":"Krasnystaw","posts":200},
    {"name":"Ksavier","location":"Grudziąc","posts":100},
    {"name":"Damian","location":"Kraków","posts":300},

]



def get_user_info(users_data: list)->None:
    for user in users_data:
        print(f"Twój znajomy {user['name']}, z miejscowości: {user['location']} opublikował {user['posts']} postów")

get_user_info(users)