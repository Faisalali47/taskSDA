print("PROGRAM NILAI AKHIR")

nama = input("Nama: ")
nim = input("NIM: ")

nilaiFormatif = float(input("Nilai Formatif: "))
nilaiUTS = float(input("Nilai UTS: "))
nilaiUAS = float(input("Nilai UAS: "))

nilaiAkhir = (
    (nilaiFormatif * 30 / 100) +
    (nilaiUTS * 30 / 100) +
    (nilaiUAS * 40 / 100)
)

if nilaiAkhir >= 80:
    nilaiHuruf = "A"
elif nilaiAkhir >= 77:
    nilaiHuruf = "A-"
elif nilaiAkhir >= 74:
    nilaiHuruf = "B+"
elif nilaiAkhir >= 70:
    nilaiHuruf = "B"
elif nilaiAkhir >= 67:
    nilaiHuruf = "B-"
elif nilaiAkhir >= 64:
    nilaiHuruf = "C+"
elif nilaiAkhir >= 60:
    nilaiHuruf = "C"
elif nilaiAkhir >= 50:
    nilaiHuruf = "D"
else:
    nilaiHuruf = "E"

print("\n===== HASIL =====")
print("Nama          :", nama)
print("NIM           :", nim)
print("Nilai Formatif:", nilaiFormatif)
print("Nilai UTS     :", nilaiUTS)
print("Nilai UAS     :", nilaiUAS)
print("Nilai Akhir   :", nilaiAkhir)
print("Nilai Huruf   :", nilaiHuruf)