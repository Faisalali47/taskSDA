print("HitungRataRata")
print("Menghitung Rata-rata N buah bilangan bulat yang dibaca dari papan ketik. N>0 "
      )
N = int(input("Masukkan jumlah bilangan: "))

jumlah = 0

for i in range(1, N + 1):
    x = int(input(f"Masukkan bilangan ke-{i}: "))
    jumlah = jumlah + x

rerata = jumlah / N

print("Rata-rata =", rerata)