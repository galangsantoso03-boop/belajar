import mysql.connector

class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connetion = None
        self.cursor = None

    def connect (self):
        try: 
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor( buffered=True)
            print("Koneksi ke database berhasil. ")
        except mysql.connector.Error as e:
            print(f"Gagal koneksi ke database: {e}")

    def login(self, username, password):
        sql = "SELECT * FROM users WHERE username = %s AND password = %s"
        self.cursor.execute(sql, (username, password))
        self.connection.commit()
        result = self.cursor.fetchone()
        if result:
            print("LOGIN BERHASIL!")
            return True
        else:   
            print("LOGIN GAGAL!")
            return False

    def create(self, nama, umur, penyakit, dokter):
        sql = "INSERT INTO pasien (nama, umur, penyakit, dokter) VALUES (%s,%s,%s, %s )"
        self.cursor.execute(sql, (nama, umur, penyakit, dokter))
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("Data pasien berhasil ditambahkan.")
        else:
            print("Gagal menambahkan data pasien.")

    def read(self):
        sql = "SELECT * FROM pasien"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        if results:
            print("Data Pasien:")
            for row in results:
                print(f"ID {row[0]}, Nama: {row[1]}, Umur: {row[2]}, Penyakit: {row[3]}, Dokter: {row[4]}")
        else: 
            print("Tidak ada data pasien.")

    def update(self, data_id, nama, umur, penyakit, dokter):
        sql = "UPDATE pasien SET nama = %s, umur = %s, penyakit = %s, dokter = %s WHERE id = %s"
        self.cursor.execute(sql, (nama, umur, penyakit, dokter, data_id))
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("Data berhasil di update.")
        else: 
            print("Gagal update data.")
    
    def delete(self, data_id):
        sql = "DELETE FROM pasien WHERE id =%s"
        self.cursor.execute(sql, (data_id,))
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("Data berhasil dihapus.")
        else:
            print("Gagal menghapus data.")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Koneksi ke database ditutup.")
