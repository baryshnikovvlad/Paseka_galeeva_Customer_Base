from datetime import datetime
import openpyxl
import pandas
from confidental import password_, password_worker
import time
from tqdm import tqdm

data_file = 'database\\dataset_xlsx.xlsx'
sheets = openpyxl.load_workbook(data_file)
sheet = sheets[sheets.sheetnames[0]]

num_of_lines_of_deals = 445  # count of deals from csv
num_of_lines_of_customers = 163
num_of_lines_of_prices = 40

#arr_deals_pandas = pandas.DataFrame(data={
#    'phone_number': [list(sheet.columns)[0][i].value for i in range(1, len(list(sheet.columns)[0]))],
#    'service': [list(sheet.columns)[1][i].value for i in range(1, len(list(sheet.columns)[1]))],
#    'count': [list(sheet.columns)[2][i].value for i in range(1, len(list(sheet.columns)[2]))]},
#    index=[pandas.to_datetime(f"{list(sheet.columns)[3][i].value}", format="%d.%m.%y") for i in range(1, len(list(sheet.columns)[3]))])
#print(arr_deals_pandas.head(5))

#arr_customers_pandas = pandas.DataFrame(data={
#    'phone_number': [list(sheet.columns)[5][i].value for i in range(1, len(list(sheet.columns)[5]))],
#    'last_name': [list(sheet.columns)[6][i].value for i in range(1, len(list(sheet.columns)[6]))],
#    'first_name': [list(sheet.columns)[7][i].value for i in range(1, len(list(sheet.columns)[7]))],
#    'father_name': [list(sheet.columns)[8][i].value for i in range(1, len(list(sheet.columns)[8]))],
#    'sex': [list(sheet.columns)[9][i].value for i in range(1, len(list(sheet.columns)[9]))],
#    'city': [list(sheet.columns)[10][i].value for i in range(1, len(list(sheet.columns)[10]))],
#    'address': [list(sheet.columns)[11][i].value for i in range(1, len(list(sheet.columns)[11]))],
#    'comment': [list(sheet.columns)[12][i].value for i in range(1, len(list(sheet.columns)[12]))]})
#print(arr_customers_pandas.head(5))

arr_prices_pandas = pandas.DataFrame(data={
    'product': [list(sheet.columns)[14][i].value for i in range(1, len(list(sheet.columns)[14]))],
    'quantity': [list(sheet.columns)[15][i].value for i in range(1, len(list(sheet.columns)[15]))],
    'price_rub': [list(sheet.columns)[16][i].value for i in range(1, len(list(sheet.columns)[16]))]
})
print(arr_prices_pandas.head(5))

import psycopg2

try:
    connection = psycopg2.connect(
        dbname='postgres',
        user='WORKER',
        password=password_worker,
        host='127.0.0.1',
        port='5432'
    )
    print('Success')
except:
    print("Can't connect to db.")

cursor = connection.cursor()

SQL_CREATE_TABLE_DEALS = """
CREATE TABLE deals IF NOT EXIST
(
    phone_number DECIMAL(11,0)
    service CHAR
    count FLOAT
    datetime TIMESTAMP
)
"""
cursor.execute(SQL_CREATE_TABLE_DEALS)

SQL_CREATE_TABLE_CUSTOMERS = """
CREATE TYPE SEX AS ENUM ('f', 'm')
CREATE TABLE customers IF NOT EXIST
(
    phone_number DECIMAL(11,0)
    last_name CHAR
    first_name CHAR
    father_name CHAR
    sex SEX
    city CHAR
    address CHAR
    comment CHAR
)
"""
cursor.execute(SQL_CREATE_TABLE_CUSTOMERS)
