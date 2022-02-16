'''
Membaca file CSV dengan menggunakan PANDAS
Bagi yang belum familiar, 
PANDAS merupakan salah satu library yang sangat sering 
digunakan untuk aplikasi dan 
implementasi data science baik 
untuk data manipulation, data 
pre-processing, atau data wrangling. 
Pada sesi kali ini, kita akan menggunakan 
PANDAS untuk membaca file dari csv.

Cobalah ketik kode di bawah ini:
'''

import pandas as pd
pd.set_option("display.max_columns",50)

table = pd.read_csv('/home/onowdev/Documents/PROJECT/Dqlab-dataAnalyst/PyDqLabs/Basic1/ReadCSVFile/Iris.csv')

table.head()
print(table)