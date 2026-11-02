import re

def validasi_nim(nim):
    return re.fullmatch(r"H071\d{6}", nim) 

def validasi_email(email):
    return re.fullmatch(r"[A-Za-z0-9._-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}", email)

def validasi_telepon(telp):
    return re.fullmatch(r"\d{10,13}", telp) 

print("=== Validasi Data Mahasiswa ===")
print()
nim = input("Masukkan NIM      : ")
email = input("Masukkan Email    : ")
telp = input("Masukkan No. Telp : ")

nim_ok = validasi_nim(nim)
email_ok = validasi_email(email)
telp_ok = validasi_telepon(telp)

print()
print("--- Hasil Validasi ---")
print("NIM         :", "Valid" if nim_ok else "Tidak valid")
print("Email       :", "Valid" if email_ok else "Tidak valid")
print("No. Telepon :", "Valid" if telp_ok else "Tidak valid")
print()

if not nim_ok:
    print("Format NIM tidak valid!")
if not email_ok:
    print("Format email tidak valid!")
if not telp_ok:
    print("Nomor telepon tidak valid!")

if nim_ok and email_ok and telp_ok:
    print("Data mahasiswa berhasil diverifikasi!")