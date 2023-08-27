def add_contact(phonebook, name, lastname, surname, phone_number):
    contacts = {
        "name": name,
        "lastname": lastname,
        "surname": surname,
        "phone_number": phone_number
        }
    phonebook.append(contacts)
    print("Контакт добавлен!")
