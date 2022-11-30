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
        cursor.execute(f"SELECT Column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME LIKE {a} and TABLE_SCHEMA  = 'ski_resort' ORDER BY ORDINAL_POSITION")
        result = cursor.fetchall()
        m = []
        for i in result:
            m.append(i[0])
        return m
    
    def get_columns_names_ru(self, table):
        d = {
            'job_title': ['id', 'название должности', 'заработная плата'],
            'hotel_room': ['id', 'номер', 'цена за ночь'],
            'track': ['id', 'название трассы', 'уровень сложности', 'цена'],
            'employee': ['id', 'имя сотрудника', 'название должности'],
            'user': ['id', 'имя пользователя', 'номер отеля'],
            'inventory': ['id', 'название инвентаря', 'цена аренды'],
            'event': ['id', 'название инвентаря', 'имя сотрудника', 'имя пользователя', 'название трассы'],
            }
        return d[table]
    
    def get_table_name_ru(self, table):
        d = {
            'job_title': 'Должности',
            'hotel_room': 'Номера отеля',
            'track': 'Трассы',
            'employee': 'Сотрудники',
            'user': 'Пользователи',
            'inventory': 'Инвентарь',
            'event': 'События',
        }
        return d[table]


    def get_table_for_print(self, table, page_number):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM {table}")
        result_1 = cursor.fetchall()
        m = []
        m_1 = []
        for i in range(len(result_1)):
            m_1.append(result_1[i])
            if len(m_1) == 10:
                m.append(m_1)
                m_1 = []
        if len(m_1) != 0:
            m.append(m_1)
        c = {
            'columns': self.get_columns_names_ru(table),
            'table_info': m[page_number],
            'number_of_pages': m,
            'table': table,
            'table_ru': self.get_table_name_ru(table),
            'page_number': page_number,
        }
        return c



    def get_table_employee(self, page_number):
        table = "employee"
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM {table}")
        result_1 = cursor.fetchall()
        table_info = []
        for i in result_1: 
            table_info.append(list(i))
        for i in range(len(table_info)): 
            cursor.execute(f"SELECT job_title_name FROM job_title where id_job_title={table_info[i][2]}")
            table_info[i][2] = cursor.fetchall()[0][0]
        m = []
        m_1 = []
        for i in range(len(table_info)):
            m_1.append(table_info[i])
            if len(m_1) == 10:
                m.append(m_1)
                m_1 = []
        if len(m_1) != 0:
            m.append(m_1)
        c = {
            'columns': self.get_columns_names_ru(table),
            'table_info': m[page_number],
            'number_of_pages': m,
            'table': table,
            'table_ru': self.get_table_name_ru(table),
            'page_number': page_number,
        }
        return c





    def get_table_user(self, page_number):
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
        m = []
        m_1 = []
        for i in range(len(table_info)):
            m_1.append(table_info[i])
            if len(m_1) == 10:
                m.append(m_1)
                m_1 = []
        if len(m_1) != 0:
            m.append(m_1)
        c = {
            'columns': self.get_columns_names_ru(table),
            'table_info': m[page_number],
            'number_of_pages': m,
            'table': table,
            'table_ru': self.get_table_name_ru(table),
            'page_number': page_number,
        }
        return c
    
    def get_table_event(self, page_number):
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
        m = []
        m_1 = []
        for i in range(len(table_info)):
            m_1.append(table_info[i])
            if len(m_1) == 10:
                m.append(m_1)
                m_1 = []
        if len(m_1) != 0:
            m.append(m_1)
        c = {
            'columns': self.get_columns_names_ru(table),
            'table_info': m[page_number],
            'number_of_pages': m,
            'table': table,
            'table_ru': self.get_table_name_ru(table),
            'page_number': page_number,
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

