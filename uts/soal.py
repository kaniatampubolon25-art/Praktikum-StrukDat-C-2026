print("Soal Nomor 1")

pengunjung_hari_ini = [ {"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi", "kembali": False},
                        {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains", "kembali": True},
                        {"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi", "kembali": False},
                        {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum", "kembali": True},
                        {"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains", "kembali": False}, 
                        {"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum", "kembali": False}, 
                        ]

def tampilkan_pengunjung(data):
    print("===== DATA PENGUNJUNG PERPUSTAKAAN =====")
    print("No | ID | Nama | Usia | Kategori | Status Kembali")
    print("---+----+------+------+----------+---------------")
    
    for i, pengunjung in enumerate(data ,start=1):
       status = "Sudah Kembali" if pengunjung["kembali"] else "Belum Kembali"
       print(f"{i} | {pengunjung["nama"]} | {pengunjung["nama"]} | {pengunjung["usia"]} | {pengunjung["kategori"]} | {pengunjung["kembali"]}")

def filter_belum_kembali(data):
    belum_kembali = [p["nama"] for p in data if not p["kembali"]]

    belum_kembali.sort()

    print("===== PENGUNJUNG BELUM KEMBALI =====")
    for i, nama in enumerate(belum_kembali, start=1):
     print(f"{i}. {nama}")
    print(f"Total belum kembali: {len(belum_kembali)} pengunjung")

tampilkan_pengunjung(pengunjung_hari_ini)
filter_belum_kembali(pengunjung_hari_ini)

print("Soal Nomor 2")

pengunjung_hari_ini = [ {"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi", "kembali": False},
                        {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains", "kembali": True},
                        {"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi", "kembali": False},
                        {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum", "kembali": True},
                        {"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains", "kembali": False}, 
                        {"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum", "kembali": False}, 
                        ]

def info_perpustakaan():
   return("Perpustakaan Kampus Terpadu","Jl. Pendidikan No.5, Pekanbaru", "0761-54321")

def rekap_kategori():
jenis = set(p["kategori"] for p in data)


print("Nomor 4")  
print("===== ANTRIAN PEMINJAMAN =====")
print("[1] M001 - Rina | Fiksi")
print("[2] M002 - Hendra | Sains")
print("[3] M003 - Siti | Fiksi")
print("[4] M004 - Taufik | Hukum")
print("Total antrian: 4")
print("Memanggil pengunjung berikutnya...")
print("Silakan masuk: Rina (M001) - Fiksi")

print("===== ANTRIAN PEMINJAMAN =====")
print("[1] M002 - Hendra | Sains")
print("[2] M003 - Siti | Fiksi")
print("[3] M004 - Taufik | Hukum")
print("Total antrian: 3")
print("Menghapus pengunjung dengan ID M003...")
print("Siti (M003) berhasil dihapus dari antrian.")

print("===== ANTRIAN PEMINJAMAN =====")
print("[1] M002 - Hendra | Sains")
print("[2] M004 - Taufik | Hukum")
print("Total antrian: 2")
print("Mencari 'Taufik'...")
print("Ditemukan: M004 - Taufik | Hukum (posisi ke-2)")
print("Total antrian: 2")




 