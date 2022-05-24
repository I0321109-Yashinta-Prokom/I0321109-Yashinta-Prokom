def luas_sisi (sisi) :
    luas = (sisi*sisi)
    print("=======================")
    print("luas bujur sangkar = ", luas)
    return(luas)

def volume_kubus(sisi):
    volume = luas_sisi(sisi)*sisi
    print("=======================")
    print("volume kubus = ", volume)
    return(volume)

def menu ():
    print("=========================")
    print(" (1) Luas Bujur Sangkar ")
    print(" (2) Volume Kubus ")
    print("=========================")


#program utama
print("Selamat datang di Program Matematika")
menu()
sisi = int(input("masukkan besaran sisi kubus = "))
pilih  = int(input("masukkan pilihan menu = "))
print("==============================")
if pilih == 1:
    luas_sisi(sisi)
else:
    volume_kubus(sisi)
