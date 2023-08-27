def show_contact(path):
    with open(path, 'r') as file:
        data = file.readlines()
    if not data:
        print("Пустой справочник")
        return

    for contact in data:
        contact = contact.strip().split('|')
        print(f'name: {contact[0]} \nlastname: {contact[1]} \nsurname: {contact[2]} \nphone-number: {contact[3]}')
        print("-" * 25)
    #     phonebook.append(
    #         {"name": contact[0], "lastname": contact[1], "surname": contact[2], "phone_number": contact[3]})
    # print(phonebook)
# show_contact('list_contact.txt')

#     if not phonebook:
#         print("Пустой справочник")
#         return
# for contact in phonebook:
#     print("*" * 26)
#     print(f'Имя: {contact["name"]} \nФамилия: {contact["lastname"]} \nОтчество: {contact["surname"]} \n'
#           f'Номер телефона: {contact["phone_number"]}')
#     print("*" * 26)
