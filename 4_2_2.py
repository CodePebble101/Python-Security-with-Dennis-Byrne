from cryptography.fernet import Fernet

# key = Fernet.generate_key()
# fernet = Fernet(key)
#
# with open("secret_key_example.txt", "wb") as file:
#     file.write(key)
#
# while True:
#     user_data = input("Введи данные для зашифровки: ")
#     print(fernet.encrypt(user_data.encode("utf8")))

# token = fernet.encrypt(b'Hello World!')
# print(token, key)
# user_token  = input("Введи токен: ")
# try:
#     print(fernet.decrypt(user_token))
# except Exception as e:
#     print(e)

user_key = input("Введи ключ шифрования: ")
fernet = Fernet(user_key)
user_choice = input("Введи команду:\n1-шифруем\n2-расшифровываем\n\n")
if user_choice == "2":
    while True:
        user_data = input("Введи данные для расшифровки: ")
        print(fernet.decrypt(user_data).decode("utf8"))
elif user_choice == "1":
    while True:
        user_data = input("Введи данные для зашифровки: ")
        print(fernet.encrypt(user_data.encode("utf8")))
