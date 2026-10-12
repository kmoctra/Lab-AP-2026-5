def bersihkan_teks(teks):
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    teks_bersih = ''    
    for char in teks.lower():
        if char in alfabet:
            teks_bersih += char
    return teks_bersih

def cek_palindrome(teks):
    teks_terbalik = ''.join(reversed(teks))
    if teks == teks_terbalik:
        return True, -1
    else:
        for i in range(len(teks)):
            if teks[i] != teks_terbalik[i]:
                return False, i

def inti_palindrome(teks_bersih):
    max_panjang = 0
    hasil_palindrom = ""
    indeks_awal = 0
    n = len(teks_bersih)

    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = teks_bersih[i:j]
            is_palin, _ = cek_palindrome(sub)
            if is_palin:
                panjang_sub = len(sub)
                if panjang_sub > max_panjang:
                    max_panjang = panjang_sub
                    hasil_palindrom = sub
                    indeks_awal = i

    return {
        "teks": hasil_palindrom,
        "panjang": max_panjang,
        "indeks_awal": indeks_awal
    }

# Program Utama
input_prasasti = input("Masukkan teks prasasti: ")
teks_bersih = bersihkan_teks(input_prasasti)
hasil = inti_palindrome(teks_bersih)

print(f"\nTeks Bersih: {teks_bersih}")
print(f"Output Terharap: {hasil}")