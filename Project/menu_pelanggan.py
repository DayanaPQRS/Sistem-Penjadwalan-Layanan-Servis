from utils import write_excel

def add_customer():
    print("\nSilakan isi data diri:")
    nama = input("Nama: ").strip()
    kontak = input("Kontak (No. HP): ").strip()
    alamat = input("Alamat: ").strip()

    # Generate ID Pelanggan berdasarkan waktu
    from datetime import datetime
    id_pelanggan = "P" + datetime.now().strftime("%Y%m%d%H%M%S")

    # Simpan data ke Excel
    write_excel('Data Pelanggan', [id_pelanggan, nama, kontak, alamat])
    print(f"Data pelanggan berhasil disimpan dengan ID: {id_pelanggan}")
    return id_pelanggan
