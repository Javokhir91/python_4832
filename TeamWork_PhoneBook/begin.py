from add_contact import add_contact
from print_contacts import show_contact
from search_contacts import search_contact
from del_contact import del_contact
# from import_contact import import_contact
print("=====Меню=====\nВыберите действие: "
      "\n1-Показать все контакты"
      "\n2-Добавить контакт"
      "\n3-Поиск контакта"
      "\n4-Внести изменения"
      "\n5-Удалить контакт"
      "\n0-Выход")



phonebook = []

data = open(r'/Users/macjava/Desktop/TeamWorkPhoneBook/fork/TeamWork_PhoneBook/list_contact.txt')
file = data.readlines()
# for contact in file:
#     contact = contact.strip().split('|')
#     phonebook.append(contact)




choice = None

# path = 'list_contact.txt'

while choice != "0":
    path = 'list_contact.txt'
    choice = input("Выберите команду: \n1-контакты/2-Добавить/3-Поиск/4-Изменить/5-Удалить/0-выход: ")
    print()
    if choice == "0":
        pass
        # with open("list_contact.txt", "a") as file:
        #     for contact in phonebook:
        #         file.write(f'{contact["name"]}|{contact["lastname"]}|{contact["surname"]}|{contact["phone_number"]}\n')

    elif choice == "1":
        show_contact(path)

    elif choice == "2":
        name = input("name: ")
        lastname = input("lastname: ")
        surname = input("surname: ")
        phone_number = input("phone_number: ")
        add_contact(phonebook, name, lastname, surname, phone_number)
        with open("list_contact.txt", "a") as file:
            for contact in phonebook:
                file.write(f'{contact["name"]}|{contact["lastname"]}|{contact["surname"]}|{contact["phone_number"]}\n')

            # for contact in phonebook:
            #     file.write((f'name: {contact[0]} \nlastname: {contact[1]} \nsurname: {contact[2]} \nphone-number: {contact[3]}'))

    elif choice == "3":
        search = input("find: ")
        print(search_contact(path, search))
        # print(search_contact("list_contact.txt", search))

    elif choice == "4":
        pass

    elif choice == "5":
        search = input("delete: ")
        del_contact(data, search)

    else:
        print("Неверный выбор. Выберите пункт из списка: ")
