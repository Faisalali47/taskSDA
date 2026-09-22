print("PROGRAM SELISIH WAKTU")
print("Menghitung selisih waktu j1 dan j2")


j1_hh = int(input("Masukkan jam pertama: "))
j1_mm = int(input("Masukkan menit pertama: "))
j1_ss = int(input("Masukkan detik pertama: "))

j2_hh = int(input("Masukkan jam kedua: "))
j2_mm = int(input("Masukkan menit kedua: "))
j2_ss = int(input("Masukkan detik kedua: "))


totalDetik1 = (j1_hh * 3600) + (j1_mm * 60) + j1_ss

totalDetik2 = (j2_hh * 3600) + (j2_mm * 60) + j2_ss

selisihDetik = totalDetik2 - totalDetik1

j3_hh = selisihDetik // 3600
sisa = selisihDetik % 3600

j3_mm = sisa // 60
j3_ss = sisa % 60

print("Selisih waktu:", j3_hh, "jam", j3_mm, "menit", j3_ss, "detik")