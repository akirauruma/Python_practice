import hashlib
import os

# хэширование пароля
password = "<PASSWORD>"
salt = os.urandom(32)
hashed_password = hashlib.pbkdf2_hmac(
    'sha256',
    password.encode('utf-8'),
    salt,
    100000,
    dklen=128
)

# добавление новой строки с N:
try:
    with open("hashed_password.txt", "r") as file:
        lines = file.readlines()
        if lines:
            last_line = lines[-1]
            user_id_counter = int(last_line.split('№:')[1].split('.\t')[0]) + 1
        else:
            user_id_counter = 1
except FileNotFoundError:
    user_id_counter = 1

# вывод хэшированного пароля в текстовик
with open("hashed_password.txt", "a") as file:
    file.write(f'User password: {hashed_password}')
print(hashed_password)

