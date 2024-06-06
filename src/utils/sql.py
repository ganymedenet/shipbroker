import psycopg2
from psycopg2 import sql
import os


# from dotenv import load_dotenv


class DBClient:
    def __init__(self):

        self.connection = None
        self.cur = None

        self.connect()

    def connect(self):

        try:
            self.connection = psycopg2.connect(
                user="postgres",
                password="admin",
                database="ships",
                host="localhost",  # Corrected host
                port="5432"  # Added port
            )

            # Create a cursor for executing SQL queries
            self.cur = self.connection.cursor()

        except Exception as e:
            print("Error connecting to PostgreSQL:", str(e))

    def exec_sql(self, sql_req, one):
        self.cur.execute(sql.SQL(sql_req))

        if one:

            results = self.cur.fetchone()
            # print(results)
        else:
            results = self.cur.fetchall()

        return results

    def exec_sql_comm(self, sql_req):
        grant_sql = """
        GRANT SELECT, INSERT ON *.* TO test;
        """

        self.cur.execute(sql_req)
        self.connection.commit()
