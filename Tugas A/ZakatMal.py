print("Hitung_Zakat")
print("Menghitung besar zakat seseorang yang kekayaannya telah melebihi nishab")

namaMuzakki = input("Masukkan Nama Muzakki: ")
nilaiKekayaan = float(input("Masukkan Nilai Kekayaan: Rp "))

zakat = 0.25 * nilaiKekayaan

print("Jumlah zakat mal yang harus dibayarkan", namaMuzakki, " = Rp ", zakat)