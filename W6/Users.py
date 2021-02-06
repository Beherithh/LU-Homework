from datetime import datetime


class User:
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email
        self.registered = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    def __str__(self):
        return (f"\tFull name: {self.name}\n \tUsername: {self.username}\n"
                f"\temail: {self.email}\n \tRegistered at: {self.registered}")


users_list = [User("Aleksey", "Alex", "alex@mail")]


def delete_user():
    del_choice = 0
    while del_choice != '1' and del_choice != '2':
        print('Enter 1 to delete by e-mail 2 to delete by username')
        del_choice = input('Your input: ')
    if del_choice == '1':
        index = find_by_mail(input('Enter email: '))
        deleting(index)
    elif del_choice == '2':
        index = find_by_username(input('Enter username: '))
        deleting(index)


def deleting(index):
    if index == -1:
        print("User not found")
    else:
        print(f'User \"{users_list[index].username}" deleted')
        users_list.pop(index)


def find():
    f_choice = 0
    while f_choice != '1' and f_choice != '2':
        print('Enter 1 to search by e-mail 2 to search by username')
        f_choice = input('Your input: ')
        if f_choice == '1':
            index = find_by_mail(input('Enter email: '))
            printing_user_data(index)
        elif f_choice == '2':
            index = find_by_username(input('Enter username: '))
            printing_user_data(index)


def printing_user_data(index):
    if index == -1:
        print("User not found")
    else:
        print(users_list[index])


def find_by_mail(mail):
    for i in users_list:
        if i.email == mail:
            return users_list.index(i)
    return -1


def find_by_username(username):
    for i in users_list:
        if i.username == username:
            return users_list.index(i)
    return -1


def add_new_user():
    print("Adding new user:")
    name = input("Full name: ")
    username = input("Username: ")
    email = input("email: ")
    users_list.append(User(name, username, email))
    print(f"New user \"{username}\" added")


choice = 0
while choice != 4:
    print('Enter 1 to print information about user, 2 to add new user, 3 to delete user, 4 to quit')
    choice = int(input('Your input: '))
    if choice == 1:
        find()
    elif choice == 2:
        add_new_user()
    elif choice == 3:
        delete_user()
print('Game over')
