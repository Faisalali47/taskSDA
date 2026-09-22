print("PROGRAM NILAI MAHASISWA")

totalNilai = 0
jumlahMahasiswa = 0
pilihan = "Y"

while pilihan == "Y":

    nama = input("\nNama Mahasiswa: ")
    nim = input("NIM: ")

    nilaiFormatif = float(input("Nilai Formatif: "))
    nilaiUTS = float(input("Nilai UTS: "))
    nilaiUAS = float(input("Nilai UAS: "))

   
    nilaiAkhir = (
        (nilaiFormatif * 30 / 100) +
        (nilaiUTS * 30 / 100) +
        (nilaiUAS * 40 / 100)
    )

    print("Nilai Akhir =", nilaiAkhir)

    
    totalNilai = totalNilai + nilaiAkhir
    jumlahMahasiswa = jumlahMahasiswa + 1

    pilihan = input("Apakah ingin input data lagi (Y/T)? ").upper()


rataRata = totalNilai / jumlahMahasiswa

print("\n=======================")
print("Jumlah Mahasiswa =", jumlahMahasiswa)
print("Rata-rata Nilai Akhir =", rataRata)