import openpyxl, os

os.chdir('G:\\Sport\\Football\\Players\\Donghai Miracle')
wb = openpyxl.load_workbook('89. Luo Cheng.xlsx', read_only = True)
ws = wb['TOTAL']

for rowOfCellObjects in ws['G3':'L15']:
    for cellObj in rowOfCellObjects:
        print(cellObj.value)
    print('--- END OF ROW ---')
