import re

def validasi_username(username):
    return re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{4,11}", username) is not None

username_valid = []

print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.")
print()

while True:
    username = input("Masukkan username: ")

    if username == "SELESAI":
        break

    if validasi_username(username):
        print("Username tersedia.")
        username_valid.append(username)
    else:
        print("Username tidak valid!")
    print()

print()
print("=== Rekapitulasi ===")
print("Username valid:")
for i, nama in enumerate(username_valid, start=1):
    print(f"{i}. {nama}")
print()
print("Jumlah username valid:", len(username_valid))