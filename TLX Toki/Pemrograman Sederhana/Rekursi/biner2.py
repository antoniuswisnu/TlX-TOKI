desimal = int(input())
hasil = ""
while (desimal != 0):
    hasil += ("%d" % (desimal%2))
    desimal //= 2
hasilakhir = ""
for i in range(len(hasil)-1,-1,-1):
    hasilakhir += hasil[i]
print(hasilakhir)