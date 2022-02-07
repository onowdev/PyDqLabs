'''	
Urutan bilangan dan teks yang diapit oleh kurung siku dan masing-masing elemennya dipisahkan dengan koma.
Contoh: [-9.52, None, True, “saya”]
mengubah tipe data lain ke tipe list
tipe data lain => tipe data list Gunakan fungsi list(Tipe data Awal)
'''
A = ("BUKU")
print(type(A))

A = list('BUKU')
print(type(A))

B = (1,2,3,4,5,6,7,8,9)

print(type(B))

B = list((1,2,3,4,5,6,7,8,9))
print(type(B))

C = {2,3,4}
print(type(C))

C = list({2,3,4})
print(type(C))