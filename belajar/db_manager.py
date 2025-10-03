import mysql.connector

class DatabaseManager:
    def __init__(self, host, user, password, database):
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
        except mysql.connector.Error as e:
            print("❌ Error:", e)

    def login(self, username, password):
        sql = "SELECT * FROM users WHERE username = %s AND password = %s"
        self.cursor.execute(sql, (username, password))
        result = self.cursor.fetchone()
        return result is not None
    
    def create(self, name, age):
        sql = "INSERT INTO data (name, age) VALUES (%s, %s)"
        self.cursor.execute(sql, (name, age))
        self.connection.commit()
        print("✅ Data inserted successfully")

    def read(self):
        self.cursor.execute("SELECT * FROM data")
        results = self.cursor.fetchall()
        for row in results:
            print(row)

    def update(self, data_id, name, age):
        sql = "UPDATE data SET name=%s, age=%s WHERE id=%s"
        self.cursor.execute(sql, (name, age, data_id))
        self.connection.commit()
        print("✅ Data updated successfully")

    def delete(self, data_id):
        sql = "DELETE FROM data WHERE id=%s"
        self.cursor.execute(sql, (data_id,))
        self.connection.commit()
        print("✅ Data deleted successfully")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close() 