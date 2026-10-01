while True:
    try :
        kursi = int(input("Masukkan maksimal kursi bus: "))
    except :
        print("Input jumlah kursi harus berupa angka! ")
        continue
    if kursi<=0 :
        print("Input jumlah kursi harus lebih dari 0")
        continue
    break

print("--- Sistem Reservasi PO BUS Dimulai ---")

sisa_kursi = kursi
total_pendapatan = 0


while sisa_kursi>0 :
    print(f"sisa kursi: {sisa_kursi}")
    try:
        umur = int(input("Masukkan umur penumpang: "))
    except:
        print("Umur tidak valid!")
        continue
    if umur <0 :
        print("Umur tidak valid!")
        continue
    if umur <= 5 :
        kategori = "Balita"
        tiketnya = 0
        print (f"Kategori:  {kategori} - Tiket gratis {tiketnya}")
    elif umur <= 12 :
        kategori = "Anak"
        tiketnya = 50000
        print (f"Kategori:  {kategori} - Tiket Rp.50.000")
    else:
        kategori = "Dewasa"
        tiketnya = 100000
        print (f"Kategori:  {kategori} - Tiket Rp.100.000")
    sisa_kursi -= 1
    total_pendapatan += tiketnya
    
print("--- Semua Kursi Terisi ---")
print(f"Total Pendapatan PO BUS kali ini : Rp. {total_pendapatan}")