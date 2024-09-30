# Nama: Ghendida Gantari Ayari
# NIM: 2409116080
# Kelas: B2024
# Tugas Mini Project Dasar Pemrograman, menghitung harga total barang berdasarkan harga barang dan jumlah pembelian

print("\n==================================================")
print("Selamat Datang dan Selamat Berbelanja Di Toko Kami")
print("==================================================\n")

while True:
    print("\nHallo Pengunjung")
    pilihan = int(input("""1. Tidak Berbelanja,
2. Berbelanja: """))
    
    if pilihan == 1:
        print("\nTerima kasih telah berkunjung!")
        break  # kluar dari program kalau tidak berbelanja

    elif pilihan == 2:
        NAMA = input("\nMasukkan Nama Anda: ")
        NIM = int(input("Masukkan NIM Anda: "))
        print("\nTerima Kasih Sudah Mengisi!")
        nama = input("Masukkan Nama Anda Lagi: ")
        nim = int(input("Masukkan NIM Anda Lagi: "))

        if NAMA == nama and NIM == nim:
            print("""\nData Berhasil Diverifikasi,
Terima Kasih""")

            while True:
                pilihan = int(input("""\n1. Kembali,
2. Hitung harga dan jumlah barang saya!: """))
                
                if pilihan == 1:
                    print("\nKembali ke menu utama.")
                    break  # kembali ke menu utama

                elif pilihan == 2:
                    harga_barang = int(input("\nHarga Barang Adalah RP. "))
                    jumlah_yang_dibeli = int(input("Jumlah Barang: "))
                    total = harga_barang * jumlah_yang_dibeli

                    if total > 250000:
                        total_diskon = total * 0.75
                        print(f"Total pembayaran setelah diskon: RP.{total_diskon}")
                    elif total < 0:
                        print("Jumlah barang tidak valid.")
                    else:
                        print(f"\nTotal pembayaran: RP.{total}")
                        print("Maaf anda tidak mendapat diskon:D")

                    # Menambahkan inputan untuk menghitung ulang
                    ulangi = input("\nApakah Anda ingin menghitung ulang lagi? (ya/tidak): ")

                    if ulangi == "ya":
                        continue  # kembali ke perhitungan
                    elif ulangi == "tidak":
                        print("\nTerima kasih sudah berbelanja di tempat kami, jangan lupa datang lagi!.")
                        break  # keluar dari loop menghitung
                    else:
                        print("\nInput tidak valid, Maaf.")
                        break  # keluar dari loop menghitung

                else:
                    print("Terdapat kesalahan coba lagi")

        else:
            print("\nMaaf, data tidak sesuai")
    else:
        print("Pilihan tidak ada")
