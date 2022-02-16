'''
kamu ingin membaca file csv yang tersimpan di direktori 
yang sama dengan direktori program python kamu, maka kode 
berikut dapat kamu gunakan (misalnya di local computer kamu): 
'''

import csv
# tentukan Lokasi File, nama file dan inisialisasi file CSV nya

f = open('/home/onowdev/Documents/PROJECT/Dqlab-dataAnalyst/PyDqLabs/Basic1/ReadCSVFile/Iris.csv', 'r')
reader = csv.reader(f)

# membaca bris per baris
for row in reader:
    print(row)
#
f.close()