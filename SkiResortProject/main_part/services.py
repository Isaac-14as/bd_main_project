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
    


    def get_columns_names(self, table):
        cursor = self.conn.cursor()
        a = f"""'{table}'"""
        cursor.execute(f"SELECT Column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME LIKE {a} and TABLE_SCHEMA  = 'ski_resort'")
        result = cursor.fetchall()
        m = []
        for i in result:
            m.append(i[0])
        return m


    def get_table_for_print(self, table):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM {table}")
        result_1 = cursor.fetchall()
        c = {
            'columns': self.get_columns_names(table),
            'table_info': result_1,
            'table': table,
        }
        return c

    def get_table_employee(self):
        table = "employee"
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM {table}")
        result_1 = cursor.fetchall()
        table_info = []
        for i in result_1: 
            table_info.append(list(i))
        print(table_info)
        for i in range(len(table_info)): 
            cursor.execute(f"SELECT job_title_name FROM job_title where id_job_title={table_info[i][2]}")
            table_info[i][2] = cursor.fetchall()[0][0]
        columns = self.get_columns_names(table)[:-1:]
        columns.append('job_title_name')
        c = {
            'columns': columns,
            'table_info': table_info,
            'table': table,
        }
        return c

    def get_table_user(self):
        table = "user"
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM {table}")
        result_1 = cursor.fetchall()
        table_info = []
        for i in result_1: 
            table_info.append(list(i))
        print(table_info)
        for i in range(len(table_info)): 
            cursor.execute(f"SELECT hotel_room_name FROM hotel_room where id_hotel_room={table_info[i][2]}")
            table_info[i][2] = cursor.fetchall()[0][0]
        columns = self.get_columns_names(table)[:-1:]
        columns.append('hotel_room_name')
        c = {
            'columns': columns,
            'table_info': table_info,
            'table': table,
        }
        return c
    
    def get_table_event(self):
        table = "event"
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM {table}")
        result_1 = cursor.fetchall()
        table_info = []
        for i in result_1: 
            table_info.append(list(i))
        print(table_info)
        for i in range(len(table_info)):
            if table_info[i][1] != None:
                cursor.execute(f"SELECT inventory_name FROM inventory where id_inventory={table_info[i][1]}")
                table_info[i][1] = cursor.fetchall()[0][0]
            if table_info[i][2] != None:
                cursor.execute(f"SELECT employee_name FROM employee where id_employee={table_info[i][2]}")
                table_info[i][2] = cursor.fetchall()[0][0]
            if table_info[i][3] != None:
                cursor.execute(f"SELECT user_name FROM user where id_user={table_info[i][3]}")
                table_info[i][3] = cursor.fetchall()[0][0]
            if table_info[i][4] != None:
                cursor.execute(f"SELECT track_name FROM track where id_track={table_info[i][4]}")
                table_info[i][4] = cursor.fetchall()[0][0]


        columns = self.get_columns_names(table)[:-4:]
        columns.append('inventory_name')
        columns.append('employee_name')
        columns.append('user_name')
        columns.append('track_name')
        c = {
            'columns': columns,
            'table_info': table_info,
            'table': table,
        }
        return c




    def delete(self, table, id):
        cursor = self.conn.cursor()
        a = 'id_' + table
        cursor.execute(f"DELETE FROM {table} WHERE {a}={id}")
        self.conn.commit()
        self.conn.close()


    def add_record(self, table, m):
        cursor = self.conn.cursor()
        values = ""
        for i in m:
            if type(i) == str:
                values += f"""'{i}'""" + ","
            else:
                values += str(i) + ","
        values = values[0:len(values) - 1]
        id = "id_" + table
        cursor.execute(f"SELECT MAX({id}) FROM {table}")
        max_id = cursor.fetchall()[0][0] + 1
        cursor.execute(f"INSERT INTO {table} VALUES ({max_id}, {values})")
        self.conn.commit()
        self.conn.close()


    def redaction_record(self, table, m, id):
        cursor = self.conn.cursor()
        bd = JobService()
        m_1 = []
        for i in bd.get_columns_names(table)[1::]:
            m_1.append(i)
        values = []
        for i in m:
            if type(i) == str:
                values.append(f"""'{i}'""")
            else:
                values.append(str(i))
        request_text = ""
        for i in range(len(m_1)):
            request_text += str(m_1[i] + ' = ' + values[i] + ', ')
        request_text = request_text[0:len(request_text) - 2]


        id_text = "id_" + table
        cursor.execute(f"UPDATE {table} SET {request_text} WHERE {id_text}={id}")
        self.conn.commit()
        self.conn.close()
    

 
    

    def get_id(self, table):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT id_{table} FROM {table}")
        result = cursor.fetchall()
        m = []
        for i in result:
            cursor.execute(f"SELECT {table}_name FROM {table} WHERE id_{table}={i[0]}")
            result_1 = cursor.fetchall()
            m.append((i[0], result_1[0][0]))
        return m

