users=[
    {"name":"Antek","location":"Zwoleń","posts":500},
    {"name":"Michał","location":"Krasnystaw","posts":200},
    {"name":"Ksavier","location":"Grudziąc","posts":100},
    {"name":"Damian","location":"Kraków","posts":300},

]

for user in users:
    print(f"Twój znajomy {user['name']}, z {user['location']} opublikował {user['posts']} postów")
