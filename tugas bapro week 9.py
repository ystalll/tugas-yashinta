import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def case1():
    class Mahasiswa:
        def __init__(self, nama, nim, prodi, nilai):
            self.nama = nama
            self.nim = nim
            self.prodi = prodi
            self.nilai = nilai

    def input_data_mahasiswa():
        clear_screen()
        mahasiswa_list = []
        jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa yang ingin diinput: "))
        for i in range(1, jumlah_mahasiswa + 1):
            print(f"\nData Mahasiswa {i}:")
            nama = input("Masukkan nama mahasiswa: ")
            nim = input("Masukkan NIM mahasiswa: ")
            prodi = input("Masukkan program studi mahasiswa: ")
            nilai = float(input("Masukkan nilai mahasiswa: "))
            mahasiswa_list.append(Mahasiswa(nama, nim, prodi, nilai))
        return mahasiswa_list

    def tampilkan_data(mahasiswa_list):
        print("\nData Mahasiswa:")
        for mahasiswa in mahasiswa_list:
            print(f"Nama: {mahasiswa.nama}, NIM: {mahasiswa.nim}, Prodi: {mahasiswa.prodi}, Nilai: {mahasiswa.nilai}")

    def hitung_rata_rata(mahasiswa_list):
        total_nilai = sum(mahasiswa.nilai for mahasiswa in mahasiswa_list)
        rata_rata = total_nilai / len(mahasiswa_list)
        print(f"Rata-rata nilai: {rata_rata}")

    def nilai_tertinggi_dan_terendah(mahasiswa_list):
        nilai_tertinggi = max(mahasiswa_list, key=lambda m: m.nilai)
        nilai_terendah = min(mahasiswa_list, key=lambda m: m.nilai)
        print(f"Mahasiswa dengan nilai tertinggi: {nilai_tertinggi.nama} dengan nilai {nilai_tertinggi.nilai}")
        print(f"Mahasiswa dengan nilai terendah: {nilai_terendah.nama} dengan nilai {nilai_terendah.nilai}")

    mahasiswa_list = input_data_mahasiswa()
    tampilkan_data(mahasiswa_list)
    hitung_rata_rata(mahasiswa_list)
    nilai_tertinggi_dan_terendah(mahasiswa_list)
    input("Tekan Enter untuk melanjutkan...")

def case2():
    class Barang:
        def __init__(self, nama_barang, kode_barang, jumlah_barang):
            self.nama_barang = nama_barang
            self.kode_barang = kode_barang
            self.jumlah_barang = jumlah_barang

    inventory = []

    def tambah_barang():
        clear_screen()
        nama_barang = input("Masukkan nama barang: ")
        kode_barang = input("Masukkan kode barang: ")
        jumlah_barang = int(input("Masukkan jumlah barang: "))
        inventory.append(Barang(nama_barang, kode_barang, jumlah_barang))
        print("Barang berhasil ditambahkan.")
        input("Tekan Enter untuk melanjutkan...")

    def tampilkan_barang():
        clear_screen()
        print("\nData Barang:")
        for barang in inventory:
            print(f"Nama Barang: {barang.nama_barang}, Kode Barang: {barang.kode_barang}, Jumlah Barang: {barang.jumlah_barang}")
        input("Tekan Enter untuk melanjutkan...")

    def cari_barang():
        clear_screen()
        kode_barang = input("Masukkan kode barang yang ingin dicari: ")
        for barang in inventory:
            if barang.kode_barang == kode_barang:
                print(f"Nama Barang: {barang.nama_barang}, Kode Barang: {barang.kode_barang}, Jumlah Barang: {barang.jumlah_barang}")
                input("Tekan Enter untuk melanjutkan...")
                return
        print("Barang tidak ditemukan.")
        input("Tekan Enter untuk melanjutkan...")

    def hapus_barang():
        clear_screen()
        kode_barang = input("Masukkan kode barang yang ingin dihapus: ")
        for barang in inventory:
            if barang.kode_barang == kode_barang:
                inventory.remove(barang)
                print("Barang berhasil dihapus.")
                input("Tekan Enter untuk melanjutkan...")
                return
        print("Barang tidak ditemukan.")
        input("Tekan Enter untuk melanjutkan...")

    while True:
        clear_screen()
        print("\nMenu Inventory Barang:")
        print("1. Tambah Barang")
        print("2. Tampilkan Barang")
        print("3. Cari Barang")
        print("4. Hapus Barang")
        print("5. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            tampilkan_barang()
        elif pilihan == '3':
            cari_barang()
        elif pilihan == '4':
            hapus_barang()
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")
            input("Tekan Enter untuk melanjutkan...")

def case3():
    class Transaksi:
        def __init__(self, tipe, jumlah):
            self.tipe = tipe
            self.jumlah = jumlah

    transaksi_list = []

    def tambah_transaksi():
        clear_screen()
        tipe = input("Masukkan tipe transaksi (pemasukan/pengeluaran): ").lower()
        jumlah = float(input("Masukkan jumlah transaksi: "))
        transaksi_list.append(Transaksi(tipe, jumlah))
        print("Transaksi berhasil ditambahkan.")
        input("Tekan Enter untuk melanjutkan...")

    def tampilkan_transaksi():
        clear_screen()
        print("\nData Transaksi:")
        for transaksi in transaksi_list:
            print(f"Tipe: {transaksi.tipe.capitalize()}, Jumlah: {transaksi.jumlah}")
        input("Tekan Enter untuk melanjutkan...")

    def hitung_total_pemasukan():
        clear_screen()
        total_pemasukan = sum(transaksi.jumlah for transaksi in transaksi_list if transaksi.tipe == 'pemasukan')
        print(f"Total Pemasukan: {total_pemasukan}")
        input("Tekan Enter untuk melanjutkan...")

    def hitung_total_pengeluaran():
        clear_screen()
        total_pengeluaran = sum(transaksi.jumlah for transaksi in transaksi_list if transaksi.tipe == 'pengeluaran')
        print(f"Total Pengeluaran: {total_pengeluaran}")
        input("Tekan Enter untuk melanjutkan...")

    def hitung_saldo_terakhir():
        clear_screen()
        saldo = sum(transaksi.jumlah if transaksi.tipe == 'pemasukan' else -transaksi.jumlah for transaksi in transaksi_list)
        print(f"Saldo Terakhir: {saldo}")
        input("Tekan Enter untuk melanjutkan...")

    while True:
        clear_screen()
        print("\nMenu Keuangan Pribadi:")
        print("1. Tambah Transaksi")
        print("2. Tampilkan Transaksi")
        print("3. Hitung Total Pemasukan")
        print("4. Hitung Total Pengeluaran")
        print("5. Hitung Saldo Terakhir")
        print("6. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tambah_transaksi()
        elif pilihan == '2':
            tampilkan_transaksi()
        elif pilihan == '3':
            hitung_total_pemasukan()
        elif pilihan == '4':
            hitung_total_pengeluaran()
        elif pilihan == '5':
            hitung_saldo_terakhir()
        elif pilihan == '6':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")
            input("Tekan Enter untuk melanjutkan...")

def main():
    while True:
        clear_screen()
        print("\nPilih Kasus:")
        print("1. Data Mahasiswa")
        print("2. Inventory Barang")
        print("3. Keuangan Pribadi")
        print("4. Keluar")
        pilihan = input("Pilih kasus: ")

        if pilihan == '1':
            case1()
        elif pilihan == '2':
            case2()
        elif pilihan == '3':
            case3()
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")
            input("Tekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()
