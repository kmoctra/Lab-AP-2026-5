def rekap_nilai(*args):
    rata_rata = sum(args) / len(args)
    nilai_tertinggi = max(args)
    nilai_terendah = min(args)

    return rata_rata, nilai_tertinggi, nilai_terendah


nilai_siswa = []

while True:
    input_nilai = input(
        "Masukkan nilai ujian siswa (kosongkan untuk selesai): "
    )

    if input_nilai == "":
        break

    nilai_siswa.append(int(input_nilai))

if len(nilai_siswa) == 0:
    print("Data nilai tidak tersedia.")
else:
    rata_rata, tertinggi, terendah = rekap_nilai(*nilai_siswa)

    print(f"Rata-rata kelas: {rata_rata}")
    print(f"Nilai tertinggi: {int(tertinggi) if tertinggi.is_integer() else tertinggi}")
    print(f"Nilai terendah: {int(terendah) if terendah.is_integer() else terendah}")