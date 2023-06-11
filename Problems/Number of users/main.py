with open('users.json', 'r') as j:
    print(len(json.load(j)['users']))
