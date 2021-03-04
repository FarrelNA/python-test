def modus(angka):
    nol=0
    terbesar=angka[0]

    for a in angka:
        jumlah=angka.count(a)
        if jumlah>=nol:
            nol=jumlah
            terbesar=a
    return(terbesar)

while True:
    a=input("masukkan list angka: ")

    angka=a.split()
    print(modus(angka))
    print("")
#Farrel Novridansyah Assjarif
#XIMIA1/15
