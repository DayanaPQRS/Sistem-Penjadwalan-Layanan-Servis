from utils import write_excel

def add_schedule(id_pelanggan, service):
    print("\nSilakan isi jadwal servis:")
    tanggal = input("Tanggal (YYYY-MM-DD): ").strip()
    waktu = input("Waktu (HH:MM): ").strip()

    # Generate ID Jadwal berdasarkan waktu
    from datetime import datetime
    id_jadwal = "J" + datetime.now().strftime("%Y%m%d%H%M%S")

    # Simpan data ke Excel
    write_excel('Jadwal Servis', [id_jadwal, tanggal, waktu, id_pelanggan, service[0], 'Menunggu'])
    print(f"Jadwal servis berhasil disimpan dengan ID: {id_jadwal}")
