from menu_servis import show_services, choose_service
from menu_pelanggan import add_customer
from menu_jadwal import add_schedule

def main():
    while True:
        print("\n===== Sistem Penjadwalan Layanan Servis =====")
        print("1. Lihat Daftar Layanan")
        print("2. Pilih Layanan Servis dan Tambah Jadwal")
        print("3. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            show_services()
        elif pilihan == '2':
            selected_service = choose_service()
            if selected_service:
                id_pelanggan = add_customer()
                add_schedule(id_pelanggan, selected_service)
        elif pilihan == '3':
            print("Terima kasih telah menggunakan sistem ini!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
