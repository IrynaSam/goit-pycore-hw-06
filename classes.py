from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if value.isdigit() and len(value) == 10:
            self.value = value
        else:
            raise ValueError("Номер має складатися з 10 цифр")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def find_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                return i
        return None
    
    def edit_phone(self, old_phone, new_phone):
        for i in self.phones:
            if i.value == old_phone:
                i.value = new_phone
                return i
        return None
    
    def remove_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                self.phones.remove(i)
        
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        
    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            return None 
        
    def delete(self, name):
        if name in self.data:
            del self.data[name]
            
            
    


