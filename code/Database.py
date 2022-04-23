import psycopg2
class Database:
    def __init__(self) -> None:
        try:
            self.conn = psycopg2.connect(
                host="localhost",
                database="postgres",
                user="postgres",
                port="5432",
                password="1234"
            )
            self.cur = self.conn.cursor()
        except Exception as error:
            print(error)
    
    def execute(self,command):
        self.cur.execute(command)
        return self.cur.fetchall()
    
    def insert(self,command):
        self.cur.execute(command)
        self.conn.commit()
