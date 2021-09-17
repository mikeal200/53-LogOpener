import os
from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days = 1)
yesterday = yesterday.strftime("%x")
yesterday = yesterday.replace('/', '.')
yesterday = yesterday.replace('0', '')
filename = yesterday + ".xlsx"
print(filename)

os.system("start EXCEL.EXE " + filename)