import random

lower_case = "abcdefghijklmopqrstuvwxyz"
upper_case = " ABCDEFGHIJKLMOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "~!@#$%^&*()_+<>?:`'/.,[]{}-="

string = lower_case + upper_case + digits + symbols
length = 16

# строк для добавления новым значениям id:
try:
    with open("passwords.txt", "r") as file:
        lines = file.readlines()
        if lines:
            last_line = lines[-1]
            user_id_counter = int(last_line.split('ID:')[1].split('.\t')[0]) + 1
        else:
            user_id_counter = 1
except FileNotFoundError:
    user_id_counter = 1


def generate_password():
    return "".join(random.sample(string, length))


# ввод логина
user_name = input("Login: ")
website = input("Website name: ")

# Генерация пароля
password = generate_password()

hashed_password = generate_password()

# добавение новых значений в файл
with open("passwords.txt", "a") as file:
    file.write(f'ID:{user_id_counter}.\tLogin: {user_name}\tWebsite: {website}\t Password: {password}\n')

print(f'For user {user_name}. (user_id: {user_id_counter}) password is: {password}')

# Инкрементирование порядкового номера пользователя
user_id_counter += 1
