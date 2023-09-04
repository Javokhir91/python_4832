from copy import deepcopy

class PhoneBook:
    def __init__(self, path: str = 'phones.txt'):
        self.path = path
        self.phone_book = {}
        self.original_book = {}


    def open_file(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for i, contact in enumerate(data, 1):
            contact = contact.strip().split(';')
            self.phone_book[i] = contact
        self.original_book = deepcopy(self.phone_book)

    def save_file(self):
        data = []
        for contact in self.phone_book.values():
            data.append(';'.join([*contact]))
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write('\n'.join(data))

    def add_contact(self, new: list[str]):
        c_id = max(self.phone_book) + 1
        self.phone_book[c_id] = new

    def search(self, word: str) -> dict[int,list[str]]:
        result = {}
        for i, contact in self.phone_book.items():
            for field in contact:
                if word.lower() in field.lower():
                    result[i] = contact
                    break
        return result

    def edit(self, c_id: int, contact: list[str]):
        current_contact = self.phone_book.get(c_id)
        new_contact = [contact[i] if contact[i] else current_contact[0] for i in range(3)]
        self.phone_book[c_id] = new_contact
        return contact[0] if contact[0] else current_contact[0]

    def del_conatact(self, c_id: int) -> list[str]:
        return self.phone_book.pop(c_id)
    