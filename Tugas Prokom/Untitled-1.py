print(range(7))
print('===========')
print(range(2,7))
for i in range(7):
    print('urutan didasarkan range=',i)

print('===============================')

bunga = ['melati', 'mawar', 'anggrek', 'kenanga', 'kamboja']
bunga.append('bakung')
bunga.insert(2,'turi')

print(len(bunga))
print(len(bunga[0]))
#cetak anggota
for b in range(0,len(bunga)):
    print('no  ',b,'bunga','   ',bunga[b])


print('===================================')
#matriks
matriksA = [[1,2],
            [3,4]]
matriksB = [[1,2,3],
            [4,5,6], 
            [7,8,9]]
matriksC = [[1,2,1,2],
            [3,4,3,4],
            [5,6,5,6]]
#matriks memanjang
print(matriksB)
#matriks kotak
for b in range(0,len(matriksB)):
    print()
    for k in range(0, len(matriksB[0])): 
        print(matriksB[b][k], end='  ')
    print()
print('=========================')