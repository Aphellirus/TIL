import hashlib

password = input("Enter password: ")

hash_pass = password.encode('utf-8')
enc_pass = hashlib.md5(hash_pass).hexdigest()

print(f"\nOriginal Password: {password}\nHash Code: {enc_pass}")
