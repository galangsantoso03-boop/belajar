import mysql.connector

class DatabaseManager:
    def __init__(self, host, user, password ,database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor(buffered=True)
            print("Koneksi ke database berhasil.")
        except mysql.connector.Error as e:
            print(f"Gagal koneksi ke database: {e}")

    
    def login(self, username, password):
        sql = "SELECT * FROM users WHERE username=%s AND password=%s"
        self.cursor.execute(sql, (username, password))
        result = self.cursor.fetchone()
        if result:
            print("LOGIN BERHASIL")
            return True
        else:
            print("LOGIN GAGAL. Username atau password salah.")
            return False

    def create(self, nama, umur, penyakit, dokter):
        sql = "INSERT INTO pasien (nama, umur, penyakit, dokter) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (nama, umur, penyakit, dokter))
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("Data berhasil ditambahkan.")
        else:
            print("Gagal menambahkan data.")

    def read(self):
        self.cursor.execute("SELECT * FROM pasien")
        results = self.cursor.fetchall()
        if results:
            print("\n=== DATA PASIEN ===")
            for row in results:
                print(f"ID: {row[0]}, Nama: {row[1]}, Umur: {row[2]}, Penyakit: {row[3]}, Dokter: {row[4]}")
        else:
            print("Tidak ada data ditemukan.")

    def update(self, data_id, nama, umur, penyakit, dokter):
        sql = "UPDATE pasien SET nama=%s, umur=%s, penyakit=%s, dokter=%s WHERE id=%s"
        self.cursor.execute(sql, (nama, umur, penyakit, dokter, data_id))
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("DATA BERHASIL DI UPDATE")
        else: 
            print("GAGAL UPDATE DATA")

    def delete(self, data_id):
        sql = "DELETE FROM pasien WHERE id=%s"
        self.cursor.execute(sql, (data_id,))
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("DATA BERHASIL DIHAPUS")
        else:
            print("GAGAL MENGHAPUS DATA")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("KONEKSI DITUTUP")
