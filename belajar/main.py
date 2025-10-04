from db_manager import DatabaseManager

def main():
    db = DatabaseManager("127.0.0.1" , "root", "", "test_db")
    db.connect()

    print("=== LOGIN SYSTEM ===")
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    
    if not db.login(username, password):
        print("LOGIN GAGAL! Username atau Password salah.")
        db.close()
        return
    else:
        print("LOGIN BERHASIL!")


    while True:
        print("\n=== MENU ===")
        print("1. Tambahkan Data")
        print("2. Lihat Data")
        print("3. Update Data")     
        print("4. Hapus Data")
        print("5. Keluar")

        pilihan = input("pilih (1-5): ")

        if pilihan == '1':
            name = input("Masukan Nama: ")
            age = input("Masukan Umur: ")
            db.create(name, age)


        elif pilihan == '2':
            db.read()

        elif pilihan == '3':
            data_id = input("Masukan ID yang ingin di update: ")
            name = input("Masukan Nama baru: ")
            age = input("Masukan Umur baru: ")
            db.update(data_id, name, age)

        elif pilihan == '4':
            data_id = input("Masukan ID yang ingin kamu hapus: ")
            db.delete(data_id)

        elif pilihan == '5':
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
