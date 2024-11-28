from utils import read_excel, load_workbook

def lihat_servis():
    data_servis = read_excel('Data Servis')
    if data_servis:
        print("\nDaftar Layanan Servis:")
        print(f"{'ID Servis':<10}{'Nama Servis':<20}{'Harga':<10}")
        for row in data_servis:
            print(f"{row[0]:<10}{row[1]:<20}{row[4]:<10}")
    else:
        print("Tidak ada data layanan untuk ditampilkan.")


def pilih_servis():
    data_servis = read_excel('Data Servis')
    if data_servis:
        lihat_servis()
        servis_id = input("\nMasukkan ID Servis yang ingin dipilih: ").strip()
        pemilihan_servis = None
        for row in data_servis:
            if row[0] == servis_id:
                pemilihan_servis = row
                break
        if pemilihan_servis:
            print("\nLayanan yang Anda pilih:")
            print(f"ID Servis        : {pemilihan_servis[0]}")
            print(f"Nama Servis      : {pemilihan_servis[1]}")
            print(f"Harga            : {pemilihan_servis[4]}")
            return pemilihan_servis
        else:
            print(f"Layanan dengan ID '{servis_id}' tidak ditemukan.")
            return None
    else:
        print("Data tidak tersedia.")
        return None


def update_status_servis():
    """
    Memperbarui status servis pada sheet 'Jadwal Servis' di file Excel.
    """
    try:
        wb = load_workbook('data_servis.xlsx')
        if 'Jadwal Servis' in wb.sheetnames:
            sheet = wb['Jadwal Servis']

            # Menampilkan data jadwal
            print("\nDaftar Jadwal Servis:")
            print(f"{'ID Jadwal':<10}{'Tanggal':<15}{'Waktu':<10}{'ID Pelanggan':<15}{'ID Servis':<10}{'Status':<10}")
            print("-" * 75)
            for row in sheet.iter_rows(min_row=2, values_only=True):
                print(f"{row[0]:<10}{row[1]:<15}{row[2]:<10}{row[3]:<15}{row[4]:<10}{row[5]:<10}")

            # Input ID Jadwal dan status baru
            id_jadwal = input("\nMasukkan ID Jadwal yang ingin diperbarui: ").strip()
            status_baru = input("Masukkan status baru (e.g., Pending, Selesai, Dibatalkan): ").strip()

            # Cari dan perbarui status
            updated = False
            for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row, min_col=1, max_col=6):
                if row[0].value == id_jadwal:
                    row[5].value = status_baru
                    updated = True
                    print(f"Status untuk ID Jadwal '{id_jadwal}' berhasil diperbarui menjadi '{status_baru}'.")
                    break

            if not updated:
                print(f"ID Jadwal '{id_jadwal}' tidak ditemukan.")

            # Simpan perubahan ke file Excel
            wb.save('data_servis.xlsx')
        else:
            print("Sheet 'Jadwal Servis' tidak ditemukan dalam file Excel.")
    except FileNotFoundError:
        print("File Excel 'data_servis.xlsx' tidak ditemukan. Pastikan file tersedia di direktori kerja.")


def delete_jadwal():
    """
    Menghapus jadwal servis berdasarkan ID Jadwal dari sheet 'Jadwal Servis' di file Excel.
    """
    try:
        wb = load_workbook('data_servis.xlsx')
        if 'Jadwal Servis' in wb.sheetnames:
            sheet = wb['Jadwal Servis']

            # Menampilkan data jadwal sebelum penghapusan
            print("\nDaftar Jadwal Servis:")
            print(f"{'ID Jadwal':<10}{'Tanggal':<15}{'Waktu':<10}{'ID Pelanggan':<15}{'ID Servis':<10}{'Status':<10}")
            print("-" * 75)
            for row in sheet.iter_rows(min_row=2, values_only=True):
                print(f"{row[0]:<10}{row[1]:<15}{row[2]:<10}{row[3]:<15}{row[4]:<10}{row[5]:<10}")

            # Meminta input ID Jadwal yang ingin dihapus
            id_jadwal = input("\nMasukkan ID Jadwal yang ingin dihapus: ").strip()

            # Mencari dan menghapus baris dengan ID Jadwal yang sesuai
            row_to_delete = None
            for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row, min_col=1, max_col=6):
                if row[0].value == id_jadwal:
                    row_to_delete = row[0].row  # Mendapatkan nomor baris untuk dihapus
                    break

            if row_to_delete:
                sheet.delete_rows(row_to_delete, 1)
                print(f"Jadwal dengan ID '{id_jadwal}' berhasil dihapus.")
            else:
                print(f"ID Jadwal '{id_jadwal}' tidak ditemukan.")

            # Simpan perubahan ke file Excel
            wb.save('data_servis.xlsx')
        else:
            print("Sheet 'Jadwal Servis' tidak ditemukan dalam file Excel.")
    except FileNotFoundError:
        print("File Excel 'data_servis.xlsx' tidak ditemukan. Pastikan file tersedia di direktori kerja.")
