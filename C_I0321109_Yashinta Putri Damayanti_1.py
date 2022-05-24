#Kendaraan yang dipilih= P= Kendaraan pribadi, B= Bus, T= Truk
#Tanggal= Jika H-1 diisi dengan 1 dan H-6 diisi dengan 6
print("====")
print(" ")
print("Selamat datang di Pintu Gerbang Tol Solo")
Jarak= int(input('Jarak yang telah ditempuh: '))
Tanggal= int(input("Kapan kamu akan tiba [jarak dengan lebaran]: "))
Kendaraan = input("Kendaraan yang digunakan:")
if Tanggal <= 5 : 
    if Kendaraan == "P" :
        print("Total Pembayaran anda adalah: " , Jarak*(0.8*1000))
    elif Kendaraan == "B" :
        print("Total Pembayaran anda adalah: " , Jarak * (0.8*1500))
    else:
        print("Total Pembayaran anda adalah: " , Jarak * (0.8*2000))
else:
    if Kendaraan == "P" :
        print("Total Pembayaran anda adalah: " , Jarak*1000)
    elif Kendaraan == "B" :
        print("Total Pembayaran anda adalah: " , Jarak *1500)
    else:
        print("Total Pembayaran anda adalah: " , Jarak *2000)