class User:
    def __init__(self, id,name,last_name,phone):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.phone = phone

    def create_email(self):
        a = str(self.name + self.last_name + '@uaprom.com')
        return a.lower()

    def show_user_info(self):
        return self.name, self.last_name, self.phone

    def update_phone(self):
        self.phone = int(input('Enter new phone number: '))
        return 'your phone is update'

user1 = User(1, 'Sasha', 'Popkins', '380969419688')
User(2, 'Dasha', 'Dupkina', '380969419667').create_email()
print(user1.create_email())
print(user1.phone)
print(user1.update_phone())
print(user1.phone)
print(user1.show_user_info())