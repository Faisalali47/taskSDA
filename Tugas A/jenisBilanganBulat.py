print("JenisBilanganBulat")
print("Menentukan apakah suatu bilangan bulat merupakan bilangan positif, negatif, atau nol")

x = int(input("Masukkan nilai x: "))

if x > 0:
    print("positif")
else:
    if x < 0:
        print("negatif")
    else:
        print("nol")