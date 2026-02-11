stok = [15, 50, 30, 25, 40]

stok.append(100)
print(stok)

stok.insert(1, 88)
print(stok)

stok.sort(reverse=True)
print(stok)

total = sum(stok)
jumlah = len(stok)
rata = total // jumlah
print("Rata-rata stok:", rata)