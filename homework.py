from collections import UserDict

class PhoneNotFoundError(Exception):
    pass

class InvalidPhoneError(Exception):
    pass

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
           raise ValueError("Please enter a phone with 10 numbers")
        super().__init__(value)	

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, value: str):
        phone = Phone(value)
        self.phones.append(phone)
    
    def remove_phone(self, value: str):
        phone = self.find_phone(value)
        if phone:
            self.phones.remove(phone)
        else:
            raise PhoneNotFoundError(f"Phone {value} not found in {self.name.value}'s record")
    
    def edit_phone(self, old_value: str, new_value: str):
        phone = self.find_phone(old_value)
        if not phone:
            raise PhoneNotFoundError(f"Phone {old_value} not found in {self.name.value}'s record")
        new_phone = Phone(new_value)
        phone.value = new_phone.value
    
    def find_phone(self, value):
        for phone in self.phones:
            if phone.value == value:
                return phone
        return None
    
    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
    
    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for record in book.data.values():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")


