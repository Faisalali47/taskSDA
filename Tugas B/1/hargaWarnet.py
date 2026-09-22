print("Program Menghitung Biaya Sewa")

jamMasuk = int(input("Jam Masuk (jam): "))
menitMasuk = int(input("Jam Masuk (menit): "))
detikMasuk = int(input("Jam Masuk (detik): "))

jamKeluar = int(input("Jam Keluar (jam): "))
menitKeluar = int(input("Jam Keluar (menit): "))
detikKeluar = int(input("Jam Keluar (detik): "))

totalDetikMasuk = (jamMasuk * 3600) + (menitMasuk * 60) + detikMasuk
totalDetikKeluar = (jamKeluar * 3600) + (menitKeluar * 60) + detikKeluar

lamaDetik = totalDetikKeluar - totalDetikMasuk

jam = lamaDetik // 3600
sisa = lamaDetik % 3600

menit = sisa // 60
detik = sisa % 60

biaya = (jam * 3000) + (menit * 500) + (detik * 10)

print("Biaya Sewanya = Rp.", biaya)