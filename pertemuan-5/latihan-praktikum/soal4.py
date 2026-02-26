gudang_pc = [
 {"item": "Monitor", "harga": 1500000, "stok": 5},
 {"item": "Keyboard", "harga": 400000, "stok": 12},
 {"item": "Mouse", "harga": 250000, "stok": 20}
]



gudang_pc.append({"item":"Headset","harga": 350000,"stok":8})
gudang_pc[1]["Kategori"] = "Aksesoris"


for x in range(len(gudang_pc)):
    print(f"item: {gudang_pc[x]["item"]} total = {gudang_pc[x]["harga"] * gudang_pc[x]["stok"]}")

