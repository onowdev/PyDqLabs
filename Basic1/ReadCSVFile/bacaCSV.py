'''
kamu ingin membaca file csv yang tersimpan di direktori 
yang sama dengan direktori program python kamu, maka kode 
berikut dapat kamu gunakan (misalnya di local computer kamu): 
'''

import csv
# tentukan Lokasi File, nama file dan inisialisasi file CSV nya

f = open('/home/onowdev/Documents/PROJECT/Dqlab-dataAnalyst/PyDqLabs/Basic1/ReadCSVFile/Iris.csv', 'r')
reader = csv.reader(f)
'''

=> tentukan lokasi file, nama file, dan inisialisasi csv
url = 'https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv'

=> baca file csv secara streaming 
with closing(requests.get(url, stream=True)) as r:
    f = (line.decode('utf-8') for line in r.iter_lines())

    reader = csv.reader(f, delimiter=',')
'''
# membaca bris per baris
for row in reader:
    print(row)
#
f.close()