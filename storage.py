import json

def pytojson(site, username, password):
    data = {
        "site": site,
        "username": username,
        "password": password
    }
    
    try:
        with open('passwords.json', 'r') as json_file:
            existing_data = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []
    
    existing_data.append(data)
    
    with open('passwords.json', 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)

def verPasswords(site):
    try:
        with open('passwords.json', 'r') as json_file:
            data = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    
    print("Passwords:")
    for entry in data:
        if entry['site'] == site:
            print(f"Site: {entry['site']}, Username: {entry['username']}, Password: {entry['password']}")
        if not any(entry['site'] == site for entry in data):
            print("Não existem palavras pass para este site.")
        