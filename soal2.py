barang = ("B001", "Laptop Gaming", 15000000)

print(barang[2])

barang_list = list(barang)        # Isi tuple tidak dapat di ubah
barang_list[2] = 14000000         #Tuple bersifat immutable (tidak bisa diubah setelah dibuat)
barang = tuple(barang_list)
print(barang)

(kode, nama, harga) = barang
print(kode)
print(nama)
print(harga)