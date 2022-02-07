'''	
Urutan bilangan dan teks yang diapit oleh kurung biasa 
dan masing-masing elemennya dipisahkan dengan koma. 
Setiap elemennya bernilai unik.
Contoh: {1, 4, 4, 3} → {1, 3, 4}

mengubah tipe data lain ke tipe set
tipe data lain => tipe data set Gunakan fungsi set(Tipe data Awal)
'''

from tkinter import PIESLICE


a = ("Buku")
print(type(a))

a = set("Buku")
print(a)
print(type(a))

b = ("SayaMakanPagi") 
print(type(b))

b = set("SayaMakanPagi")
print(b)
print(type(b))