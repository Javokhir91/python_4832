# def del_contact(phonebook, find):
#     for contact in phonebook:
#         for k, v in contact.items():
#             if find in v:  # проверяем есть ли ключ "from" в ключах словаря
#                 print('Контакт удален!')
#                 phonebook.remove(contact)
#                 break
#             else:
#                 print("Нет такого контакта!")
#     return phonebook

def del_contact(path, find):
    with open(path, 'r') as file:
        data = file.readlines()
    if not data:
        print("Пустой справочник")
        return

    for contact in data:
        contact = contact.strip().split('|')
        for i in contact:
            if i == find:
                return data.remove(contact)
    return 'Нет такого контакта!'