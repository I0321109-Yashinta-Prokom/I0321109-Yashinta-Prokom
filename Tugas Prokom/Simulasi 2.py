x = int(input("masukkan nilai x = "))
y = 1
while x != 0:
    y = x*y
    x = x-1
    print('nilai x =',x,'nilai y =', y)
print("=================================")

angka = int(input('masukkan angka dasar = '))
pangkat = int(input('masukkan nilai pangkat ='))
y = 1
while (pangkat != 0):
    y = y*angka
    pangkat = pangkat-1
print("hasil pangkat =", y)
