Nama: Ghendida Gantari Ayari
NIM: 2409116080
Kelas: B2024


![flowchartnya](https://github.com/user-attachments/assets/6a07ea6c-fe7f-4d84-9318-70fa5fca1f71)




![Screenshot (60)](https://github.com/user-attachments/assets/c528f743-bc7d-4b07-b9e1-b8afb996d805)


![Screenshot (61)](https://github.com/user-attachments/assets/bc554fe6-a08c-4517-b8fa-24584af22110)
Ini adalah jika memilih angka 1. yaitu tidak berbelanja maka akan break, dan muncul "Terima kasih telah berkunjung

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


barisan 10-13
mencetak kata "Hallo Pengunjung Menampilkan pilihan kepada pengguna, apakah ingin berbelanja atau tidak. input()
digunakan untuk mengambil pilihan dari pengguna dalam bentuk angka, dan int() mengonversi input dari string menjadi integ
print("\nHallo Pengunjung")
    pilihan = int(input("""1. Tidak Berbelanja,
2. Berbelanja: """))


barisan 15-17
kalau pengunjung memilih 1 (Tidak Berbelanja), perulangan akan dihentikan dengan break, sehingga program keluar dari loop.
if pilihan == 1:
        print("\nTerima kasih telah berkunjung!")
        break 


barisan 19-24
kalau pengunjung memilih 2 (Berbelanja), maka program akan masuk ke blok kode berikutnya untuk mengisi data pembeli.
mengambil input nama pengguna dan menyimpannya dalam variabel NAMA.
mengambil input NIM pengguna dan mengonversinya menjadi integer, disimpan dalam variabel NIM
elif pilihan == 2:
        NAMA = input("\nMasukkan Nama Anda: ")
        NIM = int(input("Masukkan NIM Anda: "))
        print("\nTerima Kasih Sudah Mengisi!")
        nama = input("Masukkan Nama Anda Lagi: ")
        nim = int(input("Masukkan NIM Anda Lagi: "))


barisan 24-28
meminta masukkan kembali nama dan NIM untuk verifikasi. Data yang diambil disimpan di variabel nama dan nim.
if NAMA == nama and NIM == nim:
            print("""\nData Berhasil Diverifikasi,
Terima Kasih""")


barisan 30-32
Menampilkan pilihan kepada pengunjung apakah ingin berbelanja atau tidak. 
input() digunakan untuk mengambil pilihan dari pengguna dalam bentuk angka, 
dan int() mengonversi input dari string menjadi integer.
 while True:
                pilihan = int(input("""\n1. Kembali,
2. Hitung harga dan jumlah barang saya!: """))


barisan 34-36
kalau pengunjung memilih 1 (Tidak Berbelanja),
perulangan akan dihentikan dengan break, sehingga program keluar dari loop.
if pilihan == 1:
                    print("\nKembali ke menu utama.")
                    break


barisan 38-41
jika pengunjung memilih 2 (Berbelanja), 
maka program akan masuk ke blok kode berikutnya untuk mengisi data pembeli.
elif pilihan == 2:
                    harga_barang = int(input("\nHarga Barang Adalah RP. "))
                    jumlah_yang_dibeli = int(input("Jumlah Barang: "))
                    total = harga_barang * jumlah_yang_dibeli


barisan 43-50
jika total harga barang lebih dari 250.000, 
diskon 25% diterapkan. 
total yang dibayar dihitung dengan mengalikan total dengan 0.75, dan hasilnya ditampilkan
kalau total kurang dari 0 (kasus yang tidak mungkin dalam perhitungan normal), program menampilkan pesan "Tidak Ada"
kalau totalnya 250.000 atau kurang, program nampilkan total tanpa diskon,dan muncul tulisan "maaf anda tidak mendapat diskon"
 if total > 250000:
                        total_diskon = total * 0.75
                        print(f"Total pembayaran setelah diskon: RP.{total_diskon}")
                    elif total < 0:
                        print("Jumlah barang tidak valid.")
                    else:
                        print(f"\nTotal pembayaran: RP.{total}")
                        print("Maaf anda tidak mendapat diskon:D")


barisan 53-62
memunculkan perulangan unttuk muncul opsi menghitung lagi atau tidak
kalau ya maka akan kembali ke perhitungan
kalau tidak maka akan muncul tulisan "Terima kasih sudah berbelanja di tempat kami, jangan lupa datang lagi!"
kalau memilih opsi yang berbeda dari pilihan akan muncul tulisan "Input tidak valid, maaf"
ulangi = input("\nApakah Anda ingin menghitung ulang lagi? (ya/tidak): ")
if ulangi == "ya":
                        continue  # kembali ke perhitungan
                    elif ulangi == "tidak":
                        print("\nTerima kasih sudah berbelanja di tempat kami, jangan lupa datang lagi!.")
                        break  # keluar dari loop menghitung
                    else:
                        print("\nInput tidak valid, Maaf.")
                        break
                        

barisan 64-65
fungsi untuk menangani kasus di mana pengunjung memasukkan input yang tidak valid ketika 
diminta untuk memilih antara menghitung (pilihan 2) atau kembali (pilihan 1), misal ke pilihan 3 yang tidak ada
else:
            print("\nMaaf, data tidak sesuai")


barisan 67-68
 Kode ini fungsi untuk memberi tahu pengguna bahwa data yang mereka masukkan tidak sesuai ketika mencoba memverifikasi nama dan NIM
print("\nMaaf, data tidak sesuai")
    else:


barisan 69-70
Kode ini digunakan untuk menangani kasus di mana pengunjung memasukkan pilihan yang tidak ada saat diminta memilih antara Tidak Berbelanja (1) 
atau Berbelanja (2). kalau pengunjung memasukkan angka selain 1 atau 2, maka program akan menampilkan pesan "Pilihan tidak ada".
else:
        print("Pilihan tidak ada")


