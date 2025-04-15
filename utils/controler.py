def get_user_info(users_data:list)->None:
    for user in users_data:
        print(f'twoj znajomy {user["name"]} z miejscowości {user["location"]} opublikował {user["posts"]} postów')
