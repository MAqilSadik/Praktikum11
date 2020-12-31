from datetime import *
def diffDate(x):
    x = x.split('-')
    tgl= date(int(x[0]),int(x[1]),int(x[2]))
    datenow = datetime.date(datetime.now())
    result = tgl - datenow
    result = result.days
    print("Tanggal sekarang     : ",datenow)
    print("Tanggal yang diminta : ",tgl)
    print("Selisih              :", result, "hari")
    return result
diffDate('2021-12-31')
