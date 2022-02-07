'''
Tipe data teks yang dapat berupa huruf, kata, frasa, 
kalimat atau paragraf yang diapit oleh ‘ atau “
'''
print("Hello World") # ini adalah tipe data String
print('Hello World') # ini Juga String

#mengubah tipe data lain ke tipe String
# tipe data lain => tipe data str Gunakan fungsi str(Tipe data Awal)

a = 7
print(type(a)) 

a = str(7)
print(type(a))

b = 9.8989
print(type(b))

b = str(9.8989)
print(type(b))

c = [1,'buku']
print(type(c))

c = str([1,'buku'])
print(type(c))