from db_manager import DatabaseManager

def main():
    db = DatabaseManager("127.0.0.1", "root" , "", "test_db")
    db.connect()

    print("=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")

    if not db.login(username, password):
        print("USERNAME ATAU PASSWORD SALAH!")
        db.close()
        return
    print("LOGIN BERHASIL")

    while True:
        print("\n=== MENU ===")
        print("1. Tambah Data Pasien")
        print("2. Lihat Data Pasien")
        print("3. Update Data Pasien")
        print("4. Hapus Data Pasien")
        print("5. Keluar")

        pilihan = input("Pilih Menu (1-5):")
        
        if pilihan == '1':
            print("\n === Tambah Data Pasien ===")
            nama = input("Nama: ")
            umur = input("Umur: ")
            penyakit = input("Penyakt: ")
            dokter = input("Dokter: ")
            db.create(nama, umur, penyakit, dokter)

        elif pilihan == '2':
            print("\n=== Lihat Data Semua Pasien ===")
            db.read()

        elif pilihan == '3':
            print("\n===Upadate data pasien ===")
            data_id = input("ID yang ingin di update: ")
            nama = input("Nama baru: ")
            umur = input("Umur baru: ")
            penyakit = input("Penyakit: ")
            dokter = input("Dokter: ")
            db.update(data_id, nama, umur, penyakit, dokter)

        elif pilihan == "4":
            print ("\n=== Hapus Data Pasien ===")
            data_id = input("ID yang ingin di hapus: ")
            db.delete(data_id)

        elif pilihan == "5":
            print("keluat dari program.")
            db.close()
            break

        else: 
            print("INPUT TIDAK VALID, SILAHKAN COBA LAGI.")

if __name__ == "__main__":
    main()
