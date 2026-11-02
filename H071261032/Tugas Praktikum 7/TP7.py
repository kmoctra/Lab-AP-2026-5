import os
import random
from datetime import datetime

FOLDER = "invoices"
RIWAYAT = "trx_history.t    xt"


def buat_id_transaksi(kasir, waktu):
    # Inisial: huruf pertama tiap kata nama kasir, huruf kapital
    inisial = "".join(kata[0] for kata in kasir.split()).upper()
    # yy mm dd HH MM -> contoh 2308291250
    bagian_waktu = waktu.strftime("%y%m%d%H%M")
    acak = random.randint(100, 999)
    return inisial + bagian_waktu + str(acak)


def input_produk():
    daftar = []
    while True:
        nama = input("Nama produk (kosongkan jika selesai): ").strip()
        if nama == "":
            if len(daftar) == 0:
                print("Minimal satu produk harus diinput.")
                continue
            break
        try:
            harga = int(input("Harga produk: "))
            jumlah = int(input("Jumlah dibeli: "))
        except ValueError:
            print("Harga dan jumlah harus berupa angka. Ulangi produk ini.")
            continue
        daftar.append((nama, harga, jumlah))
    return daftar


# ---------- SOAL 1: membuat invoice ----------
def buat_invoice(kasir, daftar_produk):
    waktu = datetime.now()
    id_trx = buat_id_transaksi(kasir, waktu)
    os.makedirs(FOLDER, exist_ok=True)  # buat folder jika belum ada

    total = 0
    garis = "=" * 50
    isi = []
    isi.append(garis)
    isi.append("INVOICE")
    isi.append(garis)
    isi.append("ID Transaksi : " + id_trx)
    isi.append("Waktu        : " + waktu.strftime("%Y-%m-%d %H:%M:%S"))
    isi.append("Kasir        : " + kasir)
    isi.append(garis)
    isi.append(f"{'Produk':<20}{'Harga':>8}{'Jml':>5}{'Subtotal':>12}")
    isi.append("-" * 50)
    for nama, harga, jumlah in daftar_produk:
        subtotal = harga * jumlah
        total += subtotal
        isi.append(f"{nama:<20}{harga:>8}{jumlah:>5}{subtotal:>12}")
    isi.append(garis)
    isi.append(f"{'TOTAL':<33}Rp. {total}")
    isi.append(garis)

    path = os.path.join(FOLDER, id_trx + ".txt")
    with open(path, "w") as f:
        f.write("\n".join(isi) + "\n")

    print("Invoice berhasil dibuat: " + path)
    return id_trx, waktu, total


# ---------- SOAL 2: mencari invoice ----------
def cari_invoice():
    id_trx = input("Masukkan ID transaksi: ").strip().upper()
    path = os.path.join(FOLDER, id_trx + ".txt")
    try:
        with open(path, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("Invoice dengan ID " + id_trx + " tidak ditemukan.")


# ---------- SOAL 3: riwayat transaksi ----------
def catat_riwayat(waktu, id_trx, total):
    garis = "=" * 66
    file_baru = not os.path.exists(RIWAYAT)
    with open(RIWAYAT, "a") as f:
        if file_baru:  # header hanya ditulis sekali
            f.write(garis + "\n")
            f.write(f"| {'Waktu':<19} | {'ID Transaksi':<20} | {'Nominal Transaksi':<17} |\n")
            f.write(garis + "\n")
        w = waktu.strftime("%Y-%m-%d %H:%M:%S")
        nominal = "Rp. " + str(total)
        f.write(f"| {w:<19} | {id_trx:<20} | {nominal:<17} |\n")
        f.write(garis + "\n")


def transaksi_baru():
    kasir = input("Nama kasir: ").strip()
    if kasir == "":
        print("Nama kasir tidak boleh kosong.")
        return
    daftar = input_produk()
    id_trx, waktu, total = buat_invoice(kasir, daftar)
    catat_riwayat(waktu, id_trx, total)
    print("Transaksi berhasil. Total: Rp. " + str(total))


def main():
    while True:
        print("\n=== APLIKASI KASIR ===")
        print("1. Transaksi baru")
        print("2. Cari invoice")
        print("3. Keluar")
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            transaksi_baru()
        elif pilihan == "2":
            cari_invoice()
        elif pilihan == "3":
            print("Terima kasih.")
            break
        else:
            print("Menu tidak valid.")


if __name__ == "__main__":
    main()