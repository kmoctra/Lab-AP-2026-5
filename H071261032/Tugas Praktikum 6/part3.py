GENRE_DIKENAL = {
    "pop": "Pop",
    "rock": "Rock", 
    "jazz": "Jazz",
    "rnb": "RnB",
    "dangdut": "Dangdut",
}
 
 
def format_durasi(detik):
    return f"{detik // 60}:{detik % 60:02d}"
 
 
def normalisasi_genre(genre):
    genre = genre.strip()
    return GENRE_DIKENAL.get(genre.lower(), genre.title())
 
 
def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    genre = normalisasi_genre(genre)
    lagu = (judul, artis, genre, durasi)
    playlist.append(lagu)
    genre_set.add(genre)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")
 
 
def tampilkan_playlist(playlist):
    if len(playlist) == 0:
        print("Playlist masih kosong.")
        return
 
    print("=" * 70)
    print(f"{'No':<4}{'Judul':<25}{'Artis':<18}{'Genre':<10}{'Durasi':<6}")
    print("=" * 70)
    total = 0
    for i, (judul, artis, genre, durasi) in enumerate(playlist, start=1):
        print(f"{i:<4}{judul:<25}{artis:<18}{genre:<10}{format_durasi(durasi):<6}")
        total += durasi
    print("=" * 70)
    print(f"Total durasi playlist: {total // 60} menit {total % 60} detik")
 
 
def filter_genre(playlist, genre_target):
    return [lagu for lagu in playlist if lagu[2].lower() == genre_target.strip().lower()]
 
 
def hapus_lagu(playlist, nomor):
    if 1 <= nomor <= len(playlist):
        lagu = playlist.pop(nomor - 1)
        print(f"Lagu '{lagu[0]}' berhasil dihapus!")
    else:
        print("Error! Nomor lagu tidak valid.")
 
 
def statistik_playlist(playlist, genre_set):
    print("=" * 40)
    print(" STATISTIK PLAYLIST PLAYTUNE")
    print("=" * 40)
 
    if len(playlist) == 0:
        print(" Playlist masih kosong.")
        print("=" * 40)
        return
 
    distribusi = {}
    for lagu in playlist:
        genre = lagu[2]
        distribusi[genre] = distribusi.get(genre, 0) + 1
 
    terpanjang = max(playlist, key=lambda lagu: lagu[3])
    terpendek = min(playlist, key=lambda lagu: lagu[3])
 
    print(f" Total lagu : {len(playlist)}")
    print(f" Jumlah genre : {len(genre_set)}")
    print(f" Daftar genre : {genre_set}")
    print(" Distribusi genre:")
    for genre, jumlah in distribusi.items():
        print(f" {genre} : {'#' * jumlah} ({jumlah})")
    print(f" Lagu terpanjang : {terpanjang[0]} ({format_durasi(terpanjang[3])})")
    print(f" Lagu terpendek : {terpendek[0]} ({format_durasi(terpendek[3])})")
    print("=" * 40)
 
 
def tampilkan_menu():
    print("Menu:")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter berdasarkan Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")
 
 
def main():
    playlist = []
    genre_set = set()
 
    print("=" * 40)
    print(" PLAYLIST MUSIK - PLAYTUNE")
    print("=" * 40)
 
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-6): ").strip()
 
        if pilihan == "1":
            judul = input("Judul lagu: ")
            artis = input("Artis: ")
            genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ")
            try:
                durasi = int(input("Durasi (dalam detik): "))
                if durasi <= 0:
                    print("Error! Durasi harus berupa angka positif.")
                else:
                    tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
            except ValueError:
                print("Error! Durasi harus berupa angka.")
 
        elif pilihan == "2":
            tampilkan_playlist(playlist)
 
        elif pilihan == "3":
            if len(genre_set) == 0:
                print("Belum ada lagu di playlist.")
            else:
                print(f"Genre tersedia: {genre_set}")
                target = input("Masukkan genre yang ingin difilter: ")
                hasil = filter_genre(playlist, target)
                if len(hasil) == 0:
                    print(f"Tidak ada lagu bergenre '{target.strip()}'.")
                else:
                    print(f"Lagu bergenre '{normalisasi_genre(target)}':")
                    for i, lagu in enumerate(hasil, start=1):
                        print(f" {i}. {lagu[0]} - {lagu[1]} ({format_durasi(lagu[3])})")
 
        elif pilihan == "4":
            if len(playlist) == 0:
                print("Playlist masih kosong.")
            else:
                tampilkan_playlist(playlist)
                try:
                    nomor = int(input("Nomor lagu yang ingin dihapus: "))
                    hapus_lagu(playlist, nomor)
                except ValueError:
                    print("Error! Nomor harus berupa angka.")
 
        elif pilihan == "5":
            statistik_playlist(playlist, genre_set)
 
        elif pilihan == "6":
            print("Terima kasih telah menggunakan PlayTune!")
            break
 
        else:
            print("Pilihan tidak valid! Masukkan angka 1-6.")
 
 
main()