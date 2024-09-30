Nama: Ghendida Gantari Ayari
NIM: 2409116080
Kelas: B2024


![flowchartnya](https://github.com/user-attachments/assets/6a07ea6c-fe7f-4d84-9318-70fa5fca1f71)


![Screenshot (60)](https://github.com/user-attachments/assets/c528f743-bc7d-4b07-b9e1-b8afb996d805)


![Screenshot (61)](https://github.com/user-attachments/assets/bc554fe6-a08c-4517-b8fa-24584af22110)


![Screenshot (62)](https://github.com/user-attachments/assets/d1b41f8a-83db-494c-a408-b8c701007f4e)


![Screenshot (63)](https://github.com/user-attachments/assets/959fc30f-caeb-41ff-86d8-64827a426112)


![Screenshot (56)](https://github.com/user-attachments/assets/aa6f245b-3683-4d86-bea4-402492920952)


![Screenshot (59)](https://github.com/user-attachments/assets/3dc5014c-f3f9-461b-afd8-811a4031e31f)



penjelasan:
Baris 6-8 adalah untuk mencetak pesan "Selamat Datang Dan Selamat Berbelanja Di Toko Kmami"
print("\n==================================================")
print("Selamat Datang dan Selamat Berbelanja Di Toko Kami")
print("==================================================\n")


baris 10
Ini adalah awal dari perulangan while yang terus berjalan hingga program menemukan kondisi
while True:

mencetak kata "Hallo Pengunjung Menampilkan pilihan kepada pengguna, apakah ingin berbelanja atau tidak. input()
digunakan untuk mengambil pilihan dari pengguna dalam bentuk angka, dan int() mengonversi input dari string menjadi integ
print("\nHallo Pengunjung")
    pilihan = int(input("""1. Tidak Berbelanja,
2. Berbelanja: """))

kalau pengunjung memilih 1 (Tidak Berbelanja), perulangan akan dihentikan dengan break, sehingga program keluar dari loop.
if pilihan == 1:
        print("\nTerima kasih telah berkunjung!")
        break 

kalau pengunjung memilih 2 (Berbelanja), maka program akan masuk ke blok kode berikutnya untuk mengisi data pembeli.
mengambil input nama pengguna dan menyimpannya dalam variabel NAMA.
mengambil input NIM pengguna dan mengonversinya menjadi integer, disimpan dalam variabel NIM
elif pilihan == 2:
        NAMA = input("\nMasukkan Nama Anda: ")
        NIM = int(input("Masukkan NIM Anda: "))
        print("\nTerima Kasih Sudah Mengisi!")
        nama = input("Masukkan Nama Anda Lagi: ")
        nim = int(input("Masukkan NIM Anda Lagi: "))

meminta masukkan kembali nama dan NIM untuk verifikasi. Data yang diambil disimpan di variabel nama dan nim.
if NAMA == nama and NIM == nim:
            print("""\nData Berhasil Diverifikasi,
Terima Kasih""")

Menampilkan pilihan kepada pengunjung apakah ingin berbelanja atau tidak. 
input() digunakan untuk mengambil pilihan dari pengguna dalam bentuk angka, 
dan int() mengonversi input dari string menjadi integer.
 while True:
                pilihan = int(input("""\n1. Kembali,
2. Hitung harga dan jumlah barang saya!: """))

kalau pengunjung memilih 1 (Tidak Berbelanja),
perulangan akan dihentikan dengan break, sehingga program keluar dari loop.
if pilihan == 1:
                    print("\nKembali ke menu utama.")
                    break


jika pengunjung memilih 2 (Berbelanja), 
maka program akan masuk ke blok kode berikutnya untuk mengisi data pembeli.
elif pilihan == 2:
                    harga_barang = int(input("\nHarga Barang Adalah RP. "))
                    jumlah_yang_dibeli = int(input("Jumlah Barang: "))
                    total = harga_barang * jumlah_yang_dibeli



