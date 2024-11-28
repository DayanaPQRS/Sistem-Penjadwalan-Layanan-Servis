from menu_servis import lihat_servis, pilih_servis
from menu_pelanggan import tambah_pelanggan
from menu_jadwal import tambah_jadwal, lihat_jadwal

def main():
    while True:
        print("\n===== Sistem Penjadwalan Layanan Servis =====")
        print("1. Lihat Daftar Layanan")
        print("2. Pilih Layanan Servis dan Tambah Jadwal")
        print("3. Lihat Jadwal Servis")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            lihat_servis()
        elif pilihan == '2':
            pemilihan_servis = pilih_servis()
            if pemilihan_servis:
                id_pelanggan = tambah_pelanggan()
                tambah_jadwal(id_pelanggan, pemilihan_servis)
        elif pilihan == '3':
            lihat_jadwal()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan sistem ini!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
