def sisaBagi(a, b):
    hasil = a % b
    return hasil


a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))

hasil = sisaBagi(a, b)

print("Sisa hasil bagi =", hasil)