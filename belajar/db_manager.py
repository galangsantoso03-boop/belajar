import mysql.connector

class DatabaseManager:
    def __init__(self, host, user, password ,database):
        self.host = host
        self.user = user
        self.password = password
        self.database =database
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
        sql = "SELECT * FROM users WHERE username = %s AND password = %s"
        self.cursor.execute(sql, (username, password))
        result = self.cursor.fetchone()
        return result is not None 

    def create(self, name, age):
        sql = "INSERT INTO data (name, age) VALUES (%s, %s)"
        self.cursor.execute(sql, (name, age))
        self.connection.commit()
        print("DATA TELAH BERHASIL DI BUAT.")

    def read(self):
        self.cursor.execute("SELECT * FROM data")
        results = self.cursor.fetchall()
        if results:
            print("=== DATA ===")
            for row in results:
                print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
        else:
            print("Tidak ada data ditemukan.")

    def update(self, data_id, name, age):
        sql = "UPDATE data SET name = %s, age = %s WHERE id = %s"
        self.cursor.execute(sql, (name, age, data_id))
        self.connection.commit()
        if self.cursor.rowcount:
            print("DATA BERHASIL DI UPDATE.")
        else:
            print("DATA TIDAK DITEMUKAN.")
    
    def delete(self, data_id):
        sql = "DELETE FROM data WHERE id = %s"
        self.cursor.execute(sql, (data_id,))
        self.connection.commit()
        if self.cursor.rowcount:
            print("DATA BERHASIL DI HAPUS. ")
        else:
            print("DATA TIDAK DITEMUKAN.")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Koneksi ke database ditutup.")
            
