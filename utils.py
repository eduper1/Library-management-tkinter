import sqlite3
from openpyxl import workbook, load_workbook

# open active excel workbook
wb = load_workbook('books.xlsx')
# open the active work sheet
ws = wb.active


# ac_cursor.execute(
#     'create table books (book_title text, book_subject text, book_qty intger, author_Lname text, author_Oname text, book_status text, comment text, register_time text)'
# )




def cal_qty(quantity, data_list):
    for i in range(1, quantity+1):
        ws.append(data_list)
        # save the workbook
        wb.save('books.xlsx')
        # re_list = [data_list]

        ac_db = sqlite3.connect('acMombasa.db')
        ac_cursor = ac_db.cursor()
        ac_cursor.execute('INSERT INTO books VALUES(?,?,?,?,?,?,?,?)', data_list)
        
        # for record in ac_cursor.execute('SELECT * FROM books'):
        #     print(record)


        ac_db.commit()
        ac_db.close()