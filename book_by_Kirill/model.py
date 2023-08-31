from copy import deepcopy

phonebook = {}
PATH = 'phones.txt'
original_book = {}


def open_file():
    global phonebook, original_book
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for i, contact in enumerate(data, 1):
        contact = contact.strip().split(';')
        phonebook[i] = contact
    original_book = deepcopy(phonebook)


def save_file():
    global phonebook
    data = []
    for contact in phonebook.values():
        data.append(';'.join([*contact]))
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(data))


def add_contact(new: list[str]):
    global phonebook
    c_id = max(phonebook) + 1
    phonebook[c_id] = new


def search(word: str) -> dict[int, list[str]]:
    global phonebook
    result = {}
    for i, contact in phonebook.items():
        for field in contact:
            if word.lower() in field.lower():
                result[i] = contact
                break
    return result


def edit(c_id: int, contact: list[str]):
    global phonebook
    current_contact = phonebook.get(c_id)
    new_contact = [contact[i] if contact[i] else current_contact[0] for i in range(3)]
    phonebook[c_id] = new_contact
    return contact[0] if contact[0] else current_contact[0]


def del_contact(c_id: int) -> list[str]:
    global phonebook
    return phonebook.pop(c_id)
