from datetime import *
def diffDate(x):
        mYFILE = open("databuku.txt",'r')
        isi = mYFILE.read()
        data = isi.replace("\n", "|")
        data = data.split("|")
        extract = data.index(kodex)
        x = x.split('-')
        x= date(int(x[0]),int(x[1]),int(x[2]))
        z = data[extract + 4].split("-")
        tglz= date(int(z[0]), int(z[1]), int(z[2]))
        result = x -tglz
        result = result.days
        return result
def carikode(kodex):
    try:
        mYFILE = open("databuku.txt",'r')
        isi = mYFILE.read()
        data = isi.replace("\n", "|")
        data = data.split("|")
        extract = data.index(kodex)
        if kodex in data :
            print('Data Peminjam Buku')
            print('Kode Member                  :', data[extract])
            print('Nama Member                  :', data[extract + 1])
            print('Judul Buku                   :', data[extract + 2])
            print('Tanggal Mulai Peminjaman     :', data[extract + 3])
            print('Tanggal Maks Peminjaman      :', data[extract + 4])
            kembali = str(input("Masukan Tanggal Pengembalian : "))
            datey = diffDate(kembali)
            if datey > 0 :
                print("Terlambat             :" ,datey,"hari")
                denda = int(datey)*2000
                print("Denda                 : Rp.",denda)
            else:
                print("Tepat Waktu !")
    
    except ValueError:
       print("Data tidak ditemukan")

ulangi = "y"
while ulangi == "y":
    kodex = input("Masukkan Kode pinjam : ")
    data = carikode(kodex)
    ulangi = input("Ulangi ? (y/n)")
    ulangi = ulangi.lower()
