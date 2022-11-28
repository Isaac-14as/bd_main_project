import pymysql

class JobService():
    def __init__(self):
        try:
            self.conn= pymysql.connect(
                host="127.0.0.1",
                port=3306,
                user='root',
                password='naz142227:Dg',
                database='ski_resort',
            )
            print('successfully connected...')
        except Exception as ex:
            print('Connectios refused...')
            print(ex)
    

    def delete(self, table, id):
        cursor = self.conn.cursor()
        a = 'id_' + table
        cursor.execute(f"DELETE FROM {table} WHERE {a}={id}")
        self.conn.commit()
        self.conn.close()

    def get_table_for_print(self, table):
        cursor = self.conn.cursor()
        a = f"""'{table}'"""
        cursor.execute(f"SELECT Column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME LIKE {a} and TABLE_SCHEMA  = 'ski_resort'")
        result = cursor.fetchall()
        cursor.execute(f"SELECT * FROM {table}")
        result_1 = cursor.fetchall()
        m = []
        for i in result:
            m.append(i[0])
        c = {
            'columns': m,
            'table_info': result_1,
            'table': table,
        }
        return c



    # def get_job_title_list(self):
    #     cursor = self.conn.cursor()
    #     cursor.execute("SELECT * FROM job_title")
    #     result = cursor.fetchall()
    #     self.conn.close()
    #     return result

    # def get_hotel_rooms_list(self):
    #     cursor = self.conn.cursor()
    #     cursor.execute("SELECT * FROM hotel_rooms")
    #     result = cursor.fetchall()
    #     self.conn.close()
    #     return result
    
    # def get_trails_list(self):
    #     cursor = self.conn.cursor()
    #     cursor.execute("SELECT * FROM trails")
    #     result = cursor.fetchall()
    #     self.conn.close()
    #     return result
    
    # def get_employees_list(self):
    #     cursor = self.conn.cursor()
    #     cursor.execute("SELECT * FROM employees")
    #     result = cursor.fetchall()
    #     self.conn.close()
    #     return result

    # def get_users_list(self):
    #     cursor = self.conn.cursor()
    #     cursor.execute("SELECT * FROM users")
    #     result = cursor.fetchall()
    #     self.conn.close()
    #     return result

    # def get_inventory_list(self):
    #     cursor = self.conn.cursor()
    #     cursor.execute("SELECT * FROM inventory")
    #     result = cursor.fetchall()
    #     self.conn.close()
    #     return result

    # def get_event_list(self):
    #     cursor = self.conn.cursor()
    #     cursor.execute("SELECT * FROM event")
    #     result = cursor.fetchall()
    #     self.conn.close()
    #     return result

    # def add_job_title(self, a, b):
    #     cursor = self.conn.cursor()
    #     a = f"""'{a}'"""
    #     cursor.execute("SELECT MAX(id_job_title) FROM job_title")
    #     max_id = cursor.fetchall()[0][0] + 1
    #     cursor.execute(f"INSERT INTO job_title VALUES ({max_id}, {a}, {b})")
    #     self.conn.commit()
    #     self.conn.close()
    





