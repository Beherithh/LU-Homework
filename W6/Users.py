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


def delete_user():
    index = find()
    if index == -1:
        print("User not found")
    else:
        print(f'User \"{users_list[index].username}" deleted')
        users_list.pop(index)


def get_info():
    index = find()
    if index == -1:
        print("User not found")
    else:
        print(users_list[index])


def find():
    f_choice = 0
    while f_choice != '1' and f_choice != '2':
        print('Enter 1 to search by e-mail 2 to search by username')
        f_choice = input('Your input: ')
    if f_choice == '1':
        return find_by_username_or_mail(None, input('Enter email: '))
    elif f_choice == '2':
        return find_by_username_or_mail(input('Enter username: '), None)


def find_by_username_or_mail(username, mail):
    for i in users_list:
        if i.username == username or i.email == mail:
            return users_list.index(i)
    return -1


def add_new_user():
    print("Adding new user:")
    name = input("Full name: ")
    username = input("Username: ")
    if find_by_username_or_mail(username, None) != -1:
        print(f'This username \'{username}\' already exists in database')
        return
    email = input("email: ")
    if find_by_username_or_mail(None, email) != -1:
        print(f'This email \'{email}\' already exists in the database')
        return
    users_list.append(User(name, username, email))
    # users_list.append(User(input("Full name: "), input("Username: "), input("email: "))) # not nice
    print(f"New user \"{username}\" added")


users_list = [User("Aleksey", "Alex", "alex@mail"), User("aa", "a", "a@a")]
choice = 0
while choice != '4':
    print('Enter 1 to print information about user, 2 to add new user, 3 to delete user, 4 to quit')
    choice = input('Your input: ')
    if choice == '1':
        get_info()
    elif choice == '2':
        add_new_user()
    elif choice == '3':
        delete_user()
print('Game over')






# Old code
# def find_by_mail(mail):
#     for i in users_list:
#         if i.email == mail:
#             return users_list.index(i)
#     return -1
#
#
# def find_by_username(username):
#     for i in users_list:
#         if i.username == username:
#             return users_list.index(i)
#     return -1