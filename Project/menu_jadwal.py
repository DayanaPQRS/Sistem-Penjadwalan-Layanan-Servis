from utils import write_excel, read_excel

def tambah_jadwal(id_pelanggan, service):
    print("\nSilakan isi jadwal servis:")
    tanggal = input("Tanggal (YYYY-MM-DD): ").strip()
    waktu = input("Waktu (HH:MM): ").strip()

    # Generate ID Jadwal berdasarkan waktu
    from datetime import datetime
    id_jadwal = "J" + datetime.now().strftime("%Y%m%d%H%M%S")

    # Simpan data ke Excel
    write_excel('Jadwal Servis', [id_jadwal, tanggal, waktu, id_pelanggan, service[0], 'Menunggu'])
    print(f"Jadwal servis berhasil disimpan dengan ID: {id_jadwal}")


def lihat_jadwal():
    """
    Menampilkan data jadwal servis dari sheet 'Jadwal Servis' dalam file Excel.
    """
    data_jadwal = read_excel('Jadwal Servis')  # Menggunakan fungsi read_excel yang sudah dibuat
    if data_jadwal:
        print("\nDaftar Jadwal Servis:")
        # Menampilkan header kolom
        print(f"{'ID Jadwal':<10}{'Tanggal':<15}{'Waktu':<10}{'ID Pelanggan':<15}{'ID Servis':<10}{'Status':<10}")
        print("-" * 75)
        # Menampilkan data jadwal
        for row in data_jadwal:
            print(f"{row[0]:<10}{row[1]:<15}{row[2]:<10}{row[3]:<15}{row[4]:<10}{row[5]:<10}")
    else:
        print("Tidak ada jadwal servis untuk ditampilkan.")
