import json

# user_input = input("Ism kiriting: ")

def new_user(user_input):
    temp = {
        "user_id": int,
        "limit":5
    }

    new_user = temp
    new_user["user_id"]=user_input

    with open('data.json', "r") as file:
        templates = json.load(file)

    templates["users"].append(new_user)

    with open('data.json', "w") as file:
        json.dump(templates, file)


