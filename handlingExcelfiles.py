import openpyxl
import xlrd
from openpyxl import workbook
path="C:/Users/shaik/PycharmProjects/seleniumPytest/EmpData.xls"
workbook=xlrd.open_workbook(path)
sheet=workbook.sheet_by_index(0)
rows=sheet.nrows
cols=sheet.ncols
for r in range (1,rows):
    print()
    for c in range(1,cols):
         print(sheet.cell(r,c).value,end="  ")



