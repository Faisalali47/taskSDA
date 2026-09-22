print("Pertukaran")
print("Mempertukarkan nilai A dan B")

A = int(input("Masukkan Nilai A: "))
B = int(input("Masukkan Nilai B: "))

print("Nilai A sebelum pertukaran = ", A)
print("Nilai B sebelum pertukaran = ", B)

A = A + B
B = A - B
A = A - B

print("Nilai A setelah pertukaran = ", A)
print("Nilai B setelah pertukaran = ", B)