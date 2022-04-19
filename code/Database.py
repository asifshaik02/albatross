import psycopg2
class Database:
    def __init__(self) -> None:
        try:
            self.conn = psycopg2.connect(
                host="127.0.0.1",
                database="albatross",
                user="postgres",
                port="5432",
                password="postgres"
            )
            self.cur = self.conn.cursor()
        except Exception as error:
            print(error)
    
    def execute(self,command):
        self.cur.execute(command)
        return self.cur.fetchall()
