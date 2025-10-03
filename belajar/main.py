from db_manager import DatabaseManager

def main():
    db = DatabaseManager("127.0.0.1", "root", "", "test_db")
    db.connect()

    print("=== LOGIN SISTEM ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if not db.login(username, password):
        print("Log in gagal. Periksa username dan password Anda.")
        db.close()
        return
    else:
        print("Log in berhasil!")

    while True:
        print("\n=== MENU ===")
        print("1. Tambahkan data")
        print("2. Tampilkan data")
        print("3. Update data")
        print("4. Hapus data")
        print("5. Logout")  
    
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            name = input("Masukkan nama: ")
            age = input("Masukkan umur: ")
            db.create(name, age)

        elif pilihan == '2':
            db.read()
    
        elif pilihan == '3':
            id = input("Masukkan ID data yang ingin diupdate: ")
            name = input("Masukkan nama baru: ")
            age = input("Masukkan umur baru: ")
            db.update(id, name, age)

        elif pilihan == '4':
            id = input("Masukkan ID data yang ingin dihapus: ")
            db.delete(id)
    
        elif pilihan == '5':
            db.close()
            print("Anda telah logout.")
            break   

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()