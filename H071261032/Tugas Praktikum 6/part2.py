def daftar_kandidat(kandidat_set, nama):
    nama = nama.strip().capitalize()
    if nama in kandidat_set:
        print(f"'{nama}' sudah terdaftar sebelumnya!")
    else:
        kandidat_set.add(nama)
        print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")
 
 
def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    kunci = nama_pemilih.strip().lower()
    nama_tampil = nama_pemilih.strip().title()
    pilihan = pilihan.strip().capitalize()
 
    if kunci in rekap_suara:
        print(f"'{nama_tampil}' sudah memberikan suara sebelumnya!")
    elif pilihan not in kandidat_set:
        print(f"Error! Kandidat '{pilihan}' tidak ada dalam daftar. "
              "Suara tidak dicatat.")
    else:
        rekap_suara[kunci] = pilihan
        print(f"Suara '{nama_tampil}' untuk '{pilihan}' berhasil dicatat!")
 
 
def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}
    for kandidat in kandidat_set:
        perolehan[kandidat] = 0
    for kandidat_dipilih in rekap_suara.values():
        perolehan[kandidat_dipilih] += 1
    return perolehan
 
 
def tampilkan_hasil(perolehan):
    print("=" * 40)
    print(" HASIL PEMILIHAN KETUA KELAS")
    print("=" * 40)
 
    # urutkan: suara terbanyak dulu, lalu berdasarkan nama
    urut = sorted(perolehan.items(), key=lambda item: (-item[1], item[0]))
    for nama, suara in urut:
        print(f" {nama}: {suara} suara")
 
    total = sum(perolehan.values())
    print(f"Total suara masuk: {total}")
 
    if total == 0:
        print("Belum ada suara yang masuk. Perlu dilakukan pemilihan ulang!")
    else:
        suara_tertinggi = max(perolehan.values())
        pemenang = [nama for nama, suara in urut if suara == suara_tertinggi]
        if len(pemenang) == 1:
            print(f"PEMENANG: {pemenang[0]} dengan {suara_tertinggi} suara!")
        else:
            print(f"Hasil SERI antara: {', '.join(pemenang)}")
            print("Perlu dilakukan pemilihan ulang!")
    print("=" * 40)
 
 
def main():
    kandidat_set = set()
    rekap_suara = {}
 
    print("=" * 40)
    print(" SISTEM PEMILIHAN KETUA KELAS")
    print("=" * 40)
 
    print("--- FASE PENDAFTARAN KANDIDAT ---")
    while True:
        nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ")
        if nama.strip() == "":
            if len(kandidat_set) < 2:
                print("Minimal harus ada 2 kandidat sebelum lanjut!")
            else:
                break
        else:
            daftar_kandidat(kandidat_set, nama)
    print(f"Kandidat terdaftar: {kandidat_set}")
 
    # ---------- Fase pemungutan suara ----------
    print("--- FASE PEMUNGUTAN SUARA ---")
    while True:
        nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ")
        if nama_pemilih.strip() == "":
            break
        print(f"Kandidat yang tersedia: {kandidat_set}")
        pilihan = input("Pilih kandidat: ")
        berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)
 
    # ---------- Hasil ----------
    perolehan = hitung_suara(rekap_suara, kandidat_set)
    tampilkan_hasil(perolehan)
 
 
main()
