from utils import write_excel, read_excel, load_workbook

def tambah_pelanggan():
    # Membaca data pelanggan dari file Excel
    data_pelanggan = read_excel('Data Pelanggan')

    # Meminta ID pelanggan untuk dicek
    print("\nApakah Anda pelanggan lama? Jika iya, masukkan ID pelanggan.")
    print("Jika tidak, biarkan kosong untuk membuat data baru.")
    id_pelanggan = input("ID Pelanggan (Kosongkan jika pelanggan baru): ").strip()

    # Mengecek apakah pelanggan lama atau baru
    if id_pelanggan and data_pelanggan:
        for row in data_pelanggan:
            if row[0] == id_pelanggan:  # Membandingkan dengan kolom ID Pelanggan
                print("\nPelanggan ditemukan!")
                print(f"Nama   : {row[1]}")
                print(f"Kontak : {row[2]}")
                print(f"Alamat : {row[3]}")
                return id_pelanggan  # Mengembalikan ID Pelanggan lama
        print(f"ID Pelanggan '{id_pelanggan}' tidak ditemukan. Silakan masukkan data baru.")

    # Jika pelanggan baru, masukkan data baru
    print("\nSilakan isi data diri:")
    nama = input("Nama: ").strip()
    kontak = input("Kontak (No. HP): ").strip()
    alamat = input("Alamat: ").strip()

    # Generate ID Pelanggan baru berdasarkan waktu
    from datetime import datetime
    id_pelanggan = "P" + datetime.now().strftime("%Y%m%d%H%M%S")

    # Simpan data ke Excel
    write_excel('Data Pelanggan', [id_pelanggan, nama, kontak, alamat])
    print(f"Data pelanggan berhasil disimpan dengan ID: {id_pelanggan}")
    return id_pelanggan


def lihat_data_pelanggan():
    """
    Menampilkan data pelanggan dari sheet 'Data Pelanggan' dalam file Excel.
    """
    data_pelanggan = read_excel('Data Pelanggan')  # Menggunakan fungsi read_excel yang sudah dibuat
    if data_pelanggan:
        print("\nDaftar Pelanggan Terdaftar:")
        # Menampilkan header kolom
        print(f"{'ID Pelanggan':<15}{'Nama':<20}{'Kontak':<15}{'Alamat':<30}")
        print("-" * 80)
        # Menampilkan data pelanggan
        for row in data_pelanggan:
            print(f"{row[0]:<15}{row[1]:<20}{row[2]:<15}{row[3]:<30}")
    else:
        print("Tidak ada data pelanggan untuk ditampilkan.")


def update_data_pelanggan():
    """
    Memperbarui data pelanggan berdasarkan ID Pelanggan.
    """
    data_pelanggan = read_excel('Data Pelanggan')
    if data_pelanggan:
        lihat_data_pelanggan()  # Tampilkan daftar pelanggan untuk referensi
        id_pelanggan = input("\nMasukkan ID Pelanggan yang ingin diperbarui: ").strip()
        updated = False

        # Periksa apakah ID Pelanggan ada dalam data
        for index, row in enumerate(data_pelanggan):
            if row[0] == id_pelanggan:
                print(f"\nData Pelanggan Lama: {row}")
                nama_baru = input("Masukkan Nama Baru (kosongkan jika tidak ingin mengubah): ").strip() or row[1]
                kontak_baru = input("Masukkan Kontak Baru (kosongkan jika tidak ingin mengubah): ").strip() or row[2]
                alamat_baru = input("Masukkan Alamat Baru (kosongkan jika tidak ingin mengubah): ").strip() or row[3]
                
                # Update data dalam list
                data_pelanggan[index] = (row[0], nama_baru, kontak_baru, alamat_baru)
                updated = True
                break
        
        if updated:
            # Tulis ulang data ke Excel
            wb = load_workbook('data_servis.xlsx')
            sheet = wb['Data Pelanggan']
            # Hapus data lama
            for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row, max_col=sheet.max_column):
                for cell in row:
                    cell.value = None
            # Tulis data baru
            for i, row in enumerate(data_pelanggan, start=2):
                for j, value in enumerate(row, start=1):
                    sheet.cell(row=i, column=j, value=value)
            wb.save('data_servis.xlsx')

            print(f"\nData pelanggan dengan ID '{id_pelanggan}' berhasil diperbarui.")
        else:
            print(f"\nPelanggan dengan ID '{id_pelanggan}' tidak ditemukan.")
    else:
        print("Data pelanggan kosong. Tidak ada yang bisa diperbarui.")

