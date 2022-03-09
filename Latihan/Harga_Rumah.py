from urllib import response
from attr import attributes
import requests
from contextlib import closing
import csv
# STEP 1: 
# Baca file "harga_rumah.txt"
url = "https://storage.googleapis.com/dqlab-dataset/harga_rumah.txt"
response = requests.get(url)
with closing(requests.get(url, stream=True)) as r:
    f = (line.decode('utf-8') for line in r.iter_lines())
    data_harga_rumah = [row for row in csv.reader(f)]
# Buat list of dict dengan nama harga rumah
key_harga_rumah = data_harga_rumah[0]
harga_rumah = []
for baris_harga_rumah in data_harga_rumah[1:]:
	dict_harga_rumah = dict()
	for i in range(len(baris_harga_rumah)):
		dict_harga_rumah[key_harga_rumah[i]] = baris_harga_rumah[i]
	harga_rumah.append(dict_harga_rumah)
print(harga_rumah)
# STEP 2:
# Buat fungsi  get_all_specified_attribute yang menerima parameter list_of_dictionary 
# (tipe data list yang berisikan sekumpulan tipe data dictionary) dan specified_key 
# (tipe data string). Fungsi akan mengembalikan sebuah list yang berisikan seluruh 
# atribut dengan kunci (key) specified_key. 
def get_all_specified_attributes(list_of_dictionary, specified_key):
	list_attributes = []
	for data in list_of_dictionary:
		attribute = data[specified_key]
		list_attributes.append(attribute)
	return list_attributes

# STEP 3: 
# Buat fungsi fungsi min_value yang menerima parameter list_attributes (berupa 
# tipe data list) dan mengembalikan nilai terkecil dalam list_attributes 
def min_value(list_attributes):
	min_attribute = 9999
	for attr in list_attributes:
		if int(attr) < min_attribute:
			min_attribute = int(attr)
	return min_attribute
# Buat fungsi dan max_value yang menerima parameter list_attribute dan 
# mengembalikan nilai terbesar dalam list_attributes.	
def max_value(list_attributes):
	max_attribute = -9999
	for attr in list_attributes:
		if int(attr) > max_attribute:
			max_attribute = int(attr)
	return max_attribute