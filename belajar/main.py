from db_manager import DatabaseManager

def main():
    db = DatabaseManager("127.0.0.1", "root", "", "test_db")
    db.connect()

    print("=== LOGIN SYSTEM ===")
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    if not db.login(username, password):
        print("LOGIN GAGAL! Username atau Password salah.")
        db.close()
        return

    print("LOGIN BERHASIL! Selamat datang di sistem klinik.")

    while True:
        print("\n=== MENU ===")
        print("1. Tambahkan Data Pasien")
        print("2. Lihat Semua Data Pasien")
        print("3. Update Data Pasien")
        print("4. Hapus Data Pasien")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            nama = input("Nama pasien: ")
            umur = input("Umur pasien: ")
            penyakit = input("Penyakit yang diderita: ")
            dokter = input("Dokter yang menangani: ")
            db.create(nama, umur, penyakit, dokter)

        elif pilihan == '2':
            db.read()

        elif pilihan == '3':
            data_id = input("Masukkan ID pasien yang ingin diupdate: ")
            nama = input("Nama baru: ")
            umur = input("Umur baru: ")
            penyakit = input("Penyakit baru: ")
            dokter = input("Dokter baru: ")
            db.update(data_id, nama, umur, penyakit, dokter)

        elif pilihan == '4':
            data_id = input("Masukkan ID pasien yang ingin dihapus: ")
            db.delete(data_id)

        elif pilihan == '5':
            print("Keluar dari program.")
            db.close()
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
