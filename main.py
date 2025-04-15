

users:list=[
    {'name':'maciej','location':'łódź','posts':100},
    {'name':'mateusz','location':'łódź','posts':200},
    {'name':'maciej81','location':'łódź','posts':300},
    {'name':'kondrad','location':'łódź','posts':400},
]


def get_user_info(users_data:list)->None:
    for user in users:
         print(f'twój znajomy {user["name"]} Maciej z miejscowości {user["location"]} opublikował {user["posts"]} postów')

get_user_info(users)