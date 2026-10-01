print("--- Rekapitulasi Transaksi Dins Store ---")
print("Ketik '0' untuk menutup toko dan mengakhiri sesi.")
 
while True:
    try:
        mads_store = int(input("Masukkan jumlah item: "))
    except:
        print("Input harus berupa angka!")
        continue
 
    if mads_store == 0:
        print("Toko ditutup. Sesi rekap selesai.")
        break
 
    if mads_store < 0:
        print("Jumlah tidak boleh negatif")
        continue
 
    if mads_store > 100:
        print("Maksimal 100 item per transaksi!")
        continue
 
    print(f"Transaksi {mads_store} item berhasil!")