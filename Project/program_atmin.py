from menu_servis import lihat_servis
from menu_pelanggan import lihat_data_pelanggan, update_data_pelanggan
from menu_servis import update_status_servis, delete_jadwal

def main():
    while True:
        print("\n===== Sistem Penjadwalan Layanan Servis =====")
        print("\n===== Menu Admin =====")
        print("1. Lihat Daftar Layanan")
        print("2. Lihat Data Pelanggan")
        print("3. Perbarui Data Pelanggan")
        print("4. Perbarui Status Servis")
        print("5. Hapus Jadwal Servis")
        print("6. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            lihat_servis()
        elif pilihan == '2':
            lihat_data_pelanggan()
        elif pilihan == '3':
            update_data_pelanggan()
        elif pilihan == '4':
            update_status_servis()
        elif pilihan == '5':
            delete_jadwal()
        elif pilihan == '6':
            print("Terima kasih telah menggunakan sistem ini!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
