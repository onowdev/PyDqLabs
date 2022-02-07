'''
Tugas Praktek
Buatlah sebuah program yang bisa mengeluarkan angka 1 sampai 10.
Tampilan akan menunjukan "Angka ganjil 1" untuk angka ganjil dan 
"Angka genap 2" untuk angka genap. (Menggunakan looping for)
'''
for i in range (1,10):
    if( i%2 == 0):
        print("Angka Genap", i)
    else:
        print("angka Ganjil", i)