from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
  def __init__(self, value):
      if len(value) == 10 and value.isdigit():
          super().__init__(value)
      else:
          raise ValueError('Valu rror')


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # cкопіювати з дз add_phonee
    def remove_phone(self):
        self.phones = [p for p in self.phones if str(p) != phone_mumber]



    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
   def add_record(self, record):
       self.data[record.name.value] = record

   def find(self, name):
       return self.data.get(name)

   def delete(self, name):
       pass
