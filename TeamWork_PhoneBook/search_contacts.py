# def search_contact(phonebook, find):
#     for contact in phonebook:
#         for v in contact.values():
#             if find.lower() in v.lower():
#                 return f'Имя:{contact["name"]} Фамилия{contact["lastname"]}|{contact["surname"]}|{contact["phone_number"]}'


def search_contact(path, find):
    with open(path, 'r') as file:
        data = file.readlines()
    if not data:
        print("Пустой справочник")
        return

    for contact in data:
        contact = contact.strip().split('|')
        for i in contact:
            if i == find:
                return contact
    return 'Нет такого контакта!'

