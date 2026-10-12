def nilai_akurat_email(email, daftar_email_valid):
    if email.count('@') != 1:
        raise ValueError("Email harus memiliki tepat satu karakter @.")

    local_part, domain_part = email.split('@')

    if not local_part or not domain_part:
        raise ValueError("Bagian local (@) atau domain (setelah @) tidak boleh kosong.")

    if ' ' in email:
        raise ValueError("Email tidak boleh mengandung spasi.")

    if email.startswith('.') or email.endswith('.'):
        raise ValueError("Email tidak boleh diawali atau diakhiri titik.")

    if '..' in email:
        raise ValueError("Email tidak boleh mengandung titik berurutan (..).")

    if '.' not in domain_part:
        raise ValueError("Bagian domain wajib memiliki minimal satu titik.")

    ekstensi_valid = ('.com', '.co.id', '.ac.id', '.org')
    if not domain_part.endswith(ekstensi_valid):
        raise ValueError("Domain wajib diakhiri dengan .com, .co.id, .ac.id, atau .org.")

    if email in daftar_email_valid:
        raise ValueError("Email sudah terdaftar (duplikat).")

    return True

def cetak_daftar_ter_email_valid_karakter():
    daftar_email_valid = []
    
    print("Sistem Pemvalidasi Email Valid")
    print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.\n")

    while True:
        input_email = input("Masukkan email: ").strip()

        if input_email.lower() == 'tutup':
            break

        try:
            if nilai_akurat_email(input_email, daftar_email_valid):
                daftar_email_valid.append(input_email)
                print("-> Email VALID dan berhasil disimpan.\n")
        except ValueError as e:
            print(f"-> Email INVALID: {e}\n")

    print("\n=== DAFTAR EMAIL VALID ===")
    if not daftar_email_valid:
        print("Tidak ada email valid yang tersimpan.")
    else:
        for mail in daftar_email_valid:
            print(f"[{mail}]")

#panggil program utama
cetak_daftar_ter_email_valid_karakter()