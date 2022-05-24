#Total Pembayaran
TotalBelanja = int(input("Masukkan Total Belanja Anda Rp = "))
Member = str(input("Apakah Anda Member? (ketik 'Ya' atau 'Bukan') = "))
if Member == "Ya" :
    if TotalBelanja > 500000 :
        Diskon = TotalBelanja * 25/100
        TotalBayar = TotalBelanja - Diskon
    elif TotalBelanja > 100000 :
        Diskon = TotalBelanja * 20/100
        TotalBayar = TotalBelanja - Diskon
    else : 
        Diskon = TotalBelanja * 10/100
        TotalBayar = TotalBelanja - Diskon
else :
    if TotalBelanja > 100000 :
        Diskon = TotalBelanja * 10/100
        TotalBayar = TotalBelanja - Diskon
    else :
        TotalBayar = TotalBelanja
print("Total Pembayaran Anda sebesar :", TotalBayar)



