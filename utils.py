from openpyxl import workbook, load_workbook

# open active excel workbook
wb = load_workbook('books.xlsx')
# open the active work sheet
ws = wb.active

def cal_qty(quantity, data_list):
    for i in range(1, quantity+1):
        ws.append(data_list)
        # save the workbook
        wb.save('books.xlsx')

