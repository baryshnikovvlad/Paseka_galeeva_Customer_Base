from datetime import datetime
import openpyxl
import pandas

data_file = 'database\\dataset_xlsx.xlsx'
sheets = openpyxl.load_workbook(data_file)
sheet = sheets[sheets.sheetnames[0]]

num_of_lines_of_deals = 445  # count of deals from csv
num_of_lines_of_customers = 163

arr_deals_pandas = pandas.DataFrame(data={
    'phone_number': [list(sheet.columns)[0][i].value for i in range(1, len(list(sheet.columns)[0]))],
    'service': [list(sheet.columns)[1][i].value for i in range(1, len(list(sheet.columns)[1]))],
    'count': [list(sheet.columns)[2][i].value for i in range(1, len(list(sheet.columns)[2]))]},
    index=[pandas.to_datetime(f"{list(sheet.columns)[3][i].value}", format="%d.%m.%y") for i in range(1, len(list(sheet.columns)[3]))])
print(arr_deals_pandas.head(5))

arr_customers_pandas = pandas.DataFrame(data={
    'phone_number': [list(sheet.columns)[5][i].value for i in range(1, len(list(sheet.columns)[5]))],
    'last_name': [list(sheet.columns)[6][i].value for i in range(1, len(list(sheet.columns)[6]))],
    'first_name': [list(sheet.columns)[7][i].value for i in range(1, len(list(sheet.columns)[7]))],
    'father_name': [list(sheet.columns)[8][i].value for i in range(1, len(list(sheet.columns)[8]))],
    'sex': [list(sheet.columns)[9][i].value for i in range(1, len(list(sheet.columns)[9]))],
    'city': [list(sheet.columns)[10][i].value for i in range(1, len(list(sheet.columns)[10]))],
    'adress': [list(sheet.columns)[11][i].value for i in range(1, len(list(sheet.columns)[11]))],
    'comment': [list(sheet.columns)[12][i].value for i in range(1, len(list(sheet.columns)[12]))]})
print(arr_customers_pandas.head(5))
