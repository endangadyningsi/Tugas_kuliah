brg = [ ]

perintah = 0                                                         

while perintah != 7:
    print('''1. menambah
2. menghapus
3. mengedit
4. menmpilkan
5. cari barang
6. cari index
7. keluar''')
    perintah = int(input("masukkan perintah: "))
    if perintah == 1:
      while True:
        elem =(input("masukkan barang: "))
        brg.append(elem)
        
        stop = input("ketik y untuk berhenti, selain itu anjut: ").lower()
        if stop == 'y' :
          break


    elif perintah == 2:
      while True:
        hps = int(input("masukkan index yang ingin di hapus: " ))
        brg.pop(hps)
        stop = input("ketik y untuk berhenti, selain itu anjut: ").lower()
        if stop == 'y' :
          break

    elif perintah == 3:
      while True:
        edit = int(input("masukkan index yang ingin di edit: " ))
        brg [edit] = input("masukkan barang yang di edit: ")
        stop = input("ketik y untuk berhenti, selain itu anjut: ").lower()
        if stop == 'y' :
          break
    elif perintah == 4:
        for i in range(len(brg)):
          print(brg[i])   
    
    elif perintah == 5:
      cari = input("cari barang: ")
      for i in range(len(brg)):
        if brg [i] == cari:
          print("barang ada dalam list: ")
print(brg)