import re

def bersihkan_nomor(nomor):
    return re.sub(r"[ -]", "", nomor)

def validasi_nomor(nomor):
    return re.fullmatch(r"\d{10,13}", nomor) is not None

print("=== Pembersihan Data Nomor Telepon ===")
print()
jumlah = int(input("Masukkan jumlah data: "))
print()

data_sebelum = []
data_sesudah = []
nomor_valid = []

for i in range(1, jumlah + 1):
    nomor = input(f"Nomor ke-{i}: ")
    print()
    data_sebelum.append(nomor)

    bersih = bersihkan_nomor(nomor)
    data_sesudah.append(bersih)

    if validasi_nomor(bersih):
        nomor_valid.append(bersih)

print("--- Hasil Pembersihan ---")
print()

for i in range(jumlah):
    status = "Valid" if validasi_nomor(data_sesudah[i]) else "Tidak valid"
    print(f"Data {i + 1}:")
    print("Sebelum :", data_sebelum[i])
    print("Sesudah :", data_sesudah[i])
    print("Status  :", status)
    print()

print("Jumlah nomor valid:", len(nomor_valid))