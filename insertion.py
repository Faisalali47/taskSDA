data = [10, 20, 30, 40, 50]
cari = 30

ditemukan = False

for i in range(len(data)):
    if data[i] == cari:
        print("Data ditemukan pada indeks", i)
        ditemukan = True
        break

if not ditemukan:
    print("Data tidak ditemukan")
    
    