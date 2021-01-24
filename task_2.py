import hashlib
from uuid import uuid4
salt = uuid4().hex
new_pass = input("Введите новый пароль: ")
hash_new_pass = hashlib.sha256(new_pass.encode()+salt.encode()).hexdigest()
print(f"Созданный хеш: {hash_new_pass}")
user_pass = input("Введите свой пароль: ")
hash_user_pass = hashlib.sha256(user_pass.encode()+salt.encode()).hexdigest()
if hash_new_pass == hash_user_pass:
    print("пароль верный")
else:
    print("Не верный пароль")