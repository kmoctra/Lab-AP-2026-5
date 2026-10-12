def konversi_suhu(suhu, skala_asal, skala_tujuan):
    skala_asal = skala_asal.upper()
    skala_tujuan = skala_tujuan.upper()

    try:
        if skala_asal not in ["C", "F", "K"]:
            raise ValueError

        if skala_tujuan not in ["C", "F", "K"]:
            raise ValueError

        # Ubah suhu asal menjadi Celsius
        if skala_asal == "C":
            celsius = suhu
        elif skala_asal == "F":
            celsius = (suhu - 32) * 5 / 9
        else:
            celsius = suhu - 273.15

        # Ubah Celsius ke skala tujuan
        if skala_tujuan == "C":
            hasil = celsius
        elif skala_tujuan == "F":
            hasil = (celsius * 9 / 5) + 32
        else:
            hasil = celsius + 273.15

        return hasil

    except ValueError:
        raise ValueError("Skala suhu tidak dikenali.")


print("=== Konversi Suhu ===")

while True:
    input_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ")

    if input_suhu.lower() == "selesai":
        break

    try:
        suhu = float(input_suhu)

        skala_asal = input("Skala asal (C/F/K): ")
        skala_tujuan = input("Skala tujuan (C/F/K): ")

        hasil = konversi_suhu(suhu, skala_asal, skala_tujuan)

        print(
            f"Hasil: {suhu} {skala_asal.upper()} = "
            f"{hasil} {skala_tujuan.upper()}"
        )

    except ValueError as error:
        if str(error) == "Skala suhu tidak dikenali.":
            print(f"Error: {error}")
        else:
            print("Input suhu harus berupa angka.")