print("Titik_Tengah")
print("menghitung nilai titik tengah dari dua buah titik P1=(X1, Y1) dan P2=(X2, Y2)")

p1_x = int(input("Masukkan koordinat P1.x: "))
p1_y = int(input("Masukkan koordinat P1.y: "))

p2_x = int(input("Masukkan koordinat P2.x: "))
p2_y = int(input("Masukkan koordinat P2.y: "))

print("(", p1_x, ",", p1_y, ")")
print("(", p2_x, ",", p2_y, ")")

p3_x = (p1_x + p2_x) / 2
p3_y = (p1_y + p2_y) / 2

print("Titik tengah koordinat p1 dan p2 adalah ", "(", p3_x, ",", p3_y, ")")