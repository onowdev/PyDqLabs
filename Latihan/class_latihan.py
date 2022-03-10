class Karyawan:
    nama_perusahaan = 'ABC'
    def __init__(self, nama, usia, pendapatan):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        if usia > 30:
            self.pendapatan += 1500000

Karyawan_1 = Karyawan('Budi', 35, 7500000)
Karyawan_2 = Karyawan('Didi', 30, 8000000)

total_pengeluaran = Karyawan_1.pendapatan + Karyawan_2.pendapatan

print(total_pengeluaran)