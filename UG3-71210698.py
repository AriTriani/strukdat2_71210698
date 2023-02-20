# Minta pengguna untuk memasukkan kalimat
kalimat = input("Masukkan kalimat: ")

# Ubah kalimat menjadi daftar kata
daftar_kata = kalimat.split()

# Buat kamus untuk menghitung setiap kata
kamus_kata = {}
for kata in daftar_kata:
    if kata in kamus_kata:
        kamus_kata[kata] += 1
    else:
        kamus_kata[kata] = 1

# Cetak jumlah setiap kata
for kata, jumlah in kamus_kata.items():
    print(f"{kata}: {jumlah}")

def hitung_kata(kalimat):
    # Menghapus karakter selain huruf dan angka
    kalimat = ''.join(e for e in kalimat if e.isalnum() or e.isspace())

    # Memisahkan kalimat menjadi kata-kata
    kata = kalimat.split()

    # Menghitung jumlah kata pada kalimat
    jumlah_kata = len(kata)

    # Menghitung jumlah kata unik pada kalimat
    kata_unik = set(kata)
    jumlah_kata_unik = len(kata_unik)

    return jumlah_kata, jumlah_kata_unik


# Contoh penggunaan
jumlah_kata, jumlah_kata_unik = hitung_kata(kalimat)

print("Total Kata:", jumlah_kata)
print("Kata Unik:", jumlah_kata_unik)

