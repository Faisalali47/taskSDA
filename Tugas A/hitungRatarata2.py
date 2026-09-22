print("HitungRataRata")
print("Menghitung rata0rata N buah bilangan bulat yang dibaca dari papan ketik. N>0")

N = int(input("Masukkan jumlah bilangan: "))

jumlah = 0
i = 1

while True:
    x = int(input("Masukkan bilangan: "))
    jumlah = jumlah + x
    i = i + 1

    if i > N:
        break

rerata = jumlah / N

print("Rata-rata =", rerata)