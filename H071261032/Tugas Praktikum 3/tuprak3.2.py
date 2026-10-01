print("--- Setup Denah Bioskop NontonYuk ---")

while True:
    try:
        baris = int(input("Masukkan jumlah baris: "))
    except:
        print("Input baris harus berupa angka!")
        continue
    if baris <= 0:
        print("Jumlah baris harus lebih dari 0!")
        continue
    break
 
while True:
    try:
        kursi = int(input("Masukkan jumlah kursi per baris: "))
    except:
        print("Input kursi harus berupa angka!")
        continue
    if kursi <= 0:
        print("Jumlah kursi harus lebih dari 0!")
        continue
    break
 
print("--- Daftar Kursi Tersedia ---")
 

for b in range(1, baris + 1):
    for k in range(1, kursi + 1):
        # Aturan Mitos: kursi 13 dilewati
        if k == 13:
            continue
        # Aturan Baris VVIP: baris 1 hanya kursi ganjil
        if b == 1 and k % 2 == 0:
            continue
        # Baris reguler: semua kursi tampil
        print(f"Baris {b} - Kursi {k}")