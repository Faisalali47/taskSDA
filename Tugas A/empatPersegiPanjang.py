import math

print("EmpatPersegiPanjang")
print("Menampilkan menu Empat Persegi Panjang, memilih menu, dan melakukan proses perhitungan")

print("Menu Empat Persegi Panjang")
print("1. Hitung Luas")
print("2. Hitung Keliling")
print("3. Hitung Panjang Diagonal")
print("4. Keluar Program")

nomorMenu = int(input("Masukkan pilihan Anda (1/2/3/4): "))

if nomorMenu == 1:
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))

    luas = panjang * lebar
    print("Luas =", luas)

elif nomorMenu == 2:
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))

    keliling = 2 * (panjang + lebar)
    print("Keliling =", keliling)

elif nomorMenu == 3:
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))

    diagonal = math.sqrt((panjang * panjang) + (lebar * lebar))
    print("Diagonal =", diagonal)

elif nomorMenu == 4:
    print("Keluar Program")

else:
    print("Pilihan tidak valid")