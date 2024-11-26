from utils import read_excel

def show_services():
    data_servis = read_excel('Data Servis')
    if data_servis:
        print("\nDaftar Layanan Servis:")
        print(f"{'ID Servis':<10}{'Nama Servis':<20}{'Harga':<10}")
        for row in data_servis:
            print(f"{row[0]:<10}{row[1]:<20}{row[4]:<10}")
    else:
        print("Tidak ada data layanan untuk ditampilkan.")

def choose_service():
    data_servis = read_excel('Data Servis')
    if data_servis:
        show_services()
        service_id = input("\nMasukkan ID Servis yang ingin dipilih: ").strip()
        selected_service = None
        for row in data_servis:
            if row[0] == service_id:
                selected_service = row
                break
        if selected_service:
            print("\nLayanan yang Anda pilih:")
            print(f"ID Servis        : {selected_service[0]}")
            print(f"Nama Servis      : {selected_service[1]}")
            print(f"Harga            : {selected_service[4]}")
            return selected_service
        else:
            print(f"Layanan dengan ID '{service_id}' tidak ditemukan.")
            return None
    else:
        print("Data tidak tersedia.")
        return None
