aalfabet = 'abcdefghijklmnopqrstuvwxyz'

def cari_katateks(teks, kata):
    indeks_ditemukan = []
    teks_lower = teks.lower()
    kata_lower = kata.lower()
    start = 0

    while True:
        pos = teks_lower.find(kata_lower, start)
        if pos == -1:
            break
        indeks_ditemukan.append(pos)
        start = pos + 1

    return indeks_ditemukan

def cek_batas_katateks(teks, i, panjang): #batas kata
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    teks_lower = teks.lower()

    if i > 0 and teks_lower[i - 1] in alfabet:
        return False

    pos_akhir = i + panjang
    if pos_akhir < len(teks_lower) and teks_lower[pos_akhir] in alfabet:
        return False

    return True

def sensor_katateks(teks, kata, simbol): #sensor
    panjang_kata = len(kata)
    semua_indeks = cari_katateks(teks, kata)
    indeks_sensor = []
    
    for idx in semua_indeks:
        if cek_batas_katateks(teks, idx, panjang_kata):
            indeks_sensor.append(idx)

    teks_hasil = ""
    i = 0
    n = len(teks)

    while i < n:
        if i in indeks_sensor:
            teks_hasil += simbol * panjang_kata
            i += panjang_kata
        else:
            teks_hasil += teks[i]
            i += 1

    return teks_hasil, len(indeks_sensor), indeks_sensor

#program Utama
teks_input = input("Masukkan Teks: ")
kata_target = input("Masukkan kata target: ")
simbol_sensor = input("Masukkan simbol: ")

hasil_teks, jumlah, daftar_indeks = sensor_katateks(teks_input, kata_target, simbol_sensor)

print(f"Hasil Teks: {hasil_teks}")
print(f"Jumlah: {jumlah} | Indeks: {daftar_indeks}")