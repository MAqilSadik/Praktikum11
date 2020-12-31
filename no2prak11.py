from datetime import *

def pinjamBuku(kode,nama,judul):
    sumber = 'databuku.txt'
    file = open('databuku.txt', 'a')
    waktu = datetime.date(datetime.now())
    waktukembali = waktu + timedelta(days=7)
    Inputlist= [kode,nama,judul,str(waktu),str(waktukembali)]
    file.write('|'.join(Inputlist)+'\n')
    file.close()

ulangi = "y"
while ulangi == "y":
    kode = input("Masukan Kode member : ")
    nama = input("Masukan Nama member : ")
    judul = input("Masukan Judul buku : ")
    pinjamBuku(kode,nama,judul)
    sumber = 'databuku.txt'
    ulangi = input("Ulangi (y/n) :")
    ulangi = ulangi.lower()
