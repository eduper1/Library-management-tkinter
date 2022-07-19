from openpyxl import workbook, load_workbook

wb = load_workbook('books.xlsx')
ws = wb.active
print(ws['A1'].value)

wb.save('books.xlsx')