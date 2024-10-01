print("Nama: Nova Rasyadina Anwar")
print("NIM: 2409116092")

#  input untuk harga barang dan jumlah pembelian
while True:
    print("masukan 0 pada harga barang, jika anda ingin keluar dari program")
    harga_barang = int(input("masukan harga barang : Rp. "))
    jumlah_barang = int(input("masukan jumlah barang yang dibeli : "))

# Menerapkan perulangan untuk memberikan pilihan apakah ingin menghitung total harga lagi atau keluar dari program
    if harga_barang == 0:
        print("program telah selesai")
        break   # keluar dari program

    total = harga_barang * jumlah_barang
    kondisi = 250000

# Membuat percabangan untuk menentukan apakah total harga barang lebih dari Rp. 250.000. Jika lebih, tambahkan diskon sebesar 25%.
    if total > kondisi:
        harga_akhir = total - (0.25 * total)
        print("selamat! anda mendapatkan diskon")
        print("total harga adalah: Rp. ",harga_akhir)
    else:
        print("total harga adalah: Rp. ",total)
        print("anda tidak dapat diskon",harga_akhir )