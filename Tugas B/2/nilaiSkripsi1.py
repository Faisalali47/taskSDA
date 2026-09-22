print("PROGRAM NILAI SKRIPSI")

nama = input("Nama Mahasiswa: ")
nim = input("NIM: ")

namaPembimbing1 = input("Nama Pembimbing I: ")
nilaiPembimbing1 = float(input("Nilai Pembimbing I: "))

namaPembimbing2 = input("Nama Pembimbing II: ")
nilaiPembimbing2 = float(input("Nilai Pembimbing II: "))

namaPenguji1 = input("Nama Penguji I: ")
nilaiPenguji1 = float(input("Nilai Penguji I: "))

namaPenguji2 = input("Nama Penguji II: ")
nilaiPenguji2 = float(input("Nilai Penguji II: "))

nilaiAkhir = (
    (nilaiPembimbing1 * 20 / 100) +
    (nilaiPembimbing2 * 20 / 100) +
    (nilaiPenguji1 * 30 / 100) +
    (nilaiPenguji2 * 30 / 100)
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
print("Nama Mahasiswa :", nama)
print("NIM             :", nim)
print("Pembimbing I    :", namaPembimbing1)
print("Nilai Pembimbing I :", nilaiPembimbing1)
print("Pembimbing II   :", namaPembimbing2)
print("Nilai Pembimbing II :", nilaiPembimbing2)
print("Penguji I       :", namaPenguji1)
print("Nilai Penguji I :", nilaiPenguji1)
print("Penguji II      :", namaPenguji2)
print("Nilai Penguji II:", nilaiPenguji2)
print("Nilai Akhir     :", nilaiAkhir)
print("Nilai Huruf     :", nilaiHuruf)