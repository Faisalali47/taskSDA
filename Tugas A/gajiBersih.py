print("Gaji_Bersih_Karyawan")
print("menghitung gaji bersih karyawan")

persenTunjangan = 0.2
persenPajak = 0.15

namaKaryawan = input("Masukkan Nama Karyawan: ")
gajiPokok = float(input("Masukkan Gaji Pokok: Rp "))

tunjangan = persenTunjangan * gajiPokok
pajak = persenPajak * gajiPokok

gajiBersih = gajiPokok + tunjangan - pajak

print("Gaji Bersih yang didapatkan", namaKaryawan, " = Rp ", gajiBersih)