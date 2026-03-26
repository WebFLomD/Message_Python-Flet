import mysql.connector
from mysql.connector import errorcode

class DataBase:
    def __init__(self):
        self.mydb = None
        self.cursor = None
        self.connectDB()
    
    # Подключение к БД
    def connectDB(self):
        try:
            self.mydb = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = '',
                database = 'msgProject'
            )
            
            self.cursor = self.mydb.cursor()
            print("Есть подключение!")

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(f"Ошибка: {err}")
            self.cursor = None

    # Поиск пользователя в БД для входа
    def checkLogin(self, username, password):
        if not self.cursor:
            return None
        try:
            self.cursor.execute("SELECT id, name FROM users WHERE username = %s AND password = %s", (username, password))
            result = self.cursor.fetchone()
        
            if result:
                userId, userName = result
                self.currentUserId = userId
                self.currentUserName = userName
                return userId, userName
            return None, None
            
        except mysql.connector.Error as err:
            print(f"Ошибка при выполнении запроса: {err}")
            return None, None

    # Получает список всех пользователей кроме текущего
    def getUserList(self):
        if not self.cursor:
            return []

        try:
            self.cursor.execute("SELECT id, name, username FROM users WHERE id != ?", (self.currentUserId))
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Ошибка при выполнении запроса: {err}")
            return []
        
    # Получает сообщения между текущим пользователем и другим пользователем
    def getMessage(self, orderUserId):
        if not self.cursor:
            return []

        try:
            self.cursor.execute(f"""
                    SELECT m.id, m.idForUsers, m.idDoUsers, m.messageText, m.date,
                    u_from.name as from_name, u_to.name as to_name 
                    FROM message m
                    JOIN users u_from ON m.idForUsers = u_from.id
                    JOIN users u_to ON m.idDoUsers = u_to.id
                    WHERE (m.idForUsers = {orderUserId} AND m.idDoUsers = {self.currentUserId})
                       OR (m.idForUsers = {self.currentUserId} AND m.idDoUsers = {orderUserId})
                    ORDER BY m.date ASC
                    """)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Ошибка при выполнении запроса: {err}")
            return []
      
    # Отправляет сообщение
    def sendMessage(self, idDoUsers, messageText):
        if not self.cursor:
            return False
        
        try:
            self.cursor.execute("INSERT INTO message (idForUsers, idDoUsers, messageText, date) VALUES (%s, %s, %s, NOW())", (self.currentUserId, idDoUsers, messageText))
            self.mydb.commit()
            return True
        
        except mysql.connector.Error as err:
            print(f"Ошибка при выполнении запроса: {err}")
            print(f"Текст сообщения: {messageText}")
            return False

        
    # def close(self):
    #     if self.cursor and self.mydb:
    #         self.cursor.close()
    #     print("Соединение закрыто!")

db = DataBase()
# db.close()