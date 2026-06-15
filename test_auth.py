from app.auth import hash_password, verify_password

password = "hello123"

hashed = hash_password(password)

print("Hash: ")
print(hashed)

print("Correct password:")
print(verify_password("hello123", hashed))

print("Wrong password:")
print(verify_password("wrong123", hashed))