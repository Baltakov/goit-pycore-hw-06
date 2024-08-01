from collections import UserDict
from re import match

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not match(r'^\d{10}$', value):
            raise ValueError('Phone number must be 10 digits')
        super().__init__(value=value)

    def __eq__(self, other):
        return isinstance(other, Phone) and self.value == other.value

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                break
        else:
            raise ValueError(f'Phone number {phone} does not belong to record {self.name}')

    def edit_phone(self, old_phone: str, new_phone: str):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break
        else:
            raise ValueError(f'Phone number {old_phone} does not belong to record {self.name}')

    def find_phone(self, phone: str) -> Phone:
        for phone_field in self.phones:
            if phone_field.value == phone:
                return phone_field
        raise ValueError(f'Phone number {phone} does not belong to record {self.name}')

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[str(record.name)] = record

    def find(self, name: str) -> Record:
        if name not in self.data:
            raise ValueError('Record not found')
        return self.data[name]

    def delete(self, name: str):
        if name not in self.data:
            raise ValueError('Record not found')
        self.data.pop(name)
