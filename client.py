import requests

URL = "http://localhost:5000/document"

while True:
    print("\n1 - Create")
    print("2 - Update")
    print("3 - Delete")
    print("4 - Exit")

    option = input("Choose: ")

    if option == "4":
        break

    key = input("Key: ")

    data = {}

    if option == "1":
        value = input("Value: ")
        data = {"action": "create", "key": key, "value": value}

    elif option == "2":
        value = input("Value: ")
        data = {"action": "update", "key": key, "value": value}

    elif option == "3":
        data = {"action": "delete", "key": key}

    else:
        print("Invalid option")
        continue

    response = requests.post(URL, json=data)
    print("Response:", response.json())