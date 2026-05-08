class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, kode):
        total = sum(ord(char) for char in kode)
        return total % self.size
    
    def insert(self, kode, judul):
        index = self.hash_function(kode)
        bucket = self.table[index]

        for i in range(len(bucket)):
            if bucket[i][1] == kode:
                bucket[i][1] = judul
                print(f"Data dengan kode {kode} berhasil diupdate")
                return
            
        bucket.append([kode, judul])
        print(f"Data {kode} berhasil ditambahkan")

    def search(self, kode):
        index = self.hash_function(kode)
        bucket = self.table[index]

        for item in bucket:
            if item[0] == kode:
                print(f"{kode} : {item[1]}")
                return
            
        print("Buku tidak ditemukan")

    def delete(self, kode):
        index = self.hash_function(kode)
        bucket = self.table[index]

        for item in bucket:
            if item[0] == kode:
                bucket.remove(item)
                print(f"Data {kode} berhasil dihapus")
                return
            
        print("Buku tidak ditemukan")

    def display(self):
        print("\nISI HASH TABLE")
        for i in range(self.size):
            print(f"Bucket {i} :", end=" ")

            if len(self.table[i]) == 0:
                print("Kosong")
            else:
                for item in self.table[i]:
                    print(f"[{item[0]} : {item[1]}]", end=" ")
                print()

buku = HashTable()

# insert 
buku.insert("BK111", "Mahir C++ Dalam Satu Jam")
buku.insert("BK222", "Python Dasar")
buku.insert("BK333", "Matematika Diskrit")
buku.insert("BK444", "Atomic Habits")
buku.insert("BK555", "Sruktur Data")

# display
buku.display()

# insert baru
print("\n=== INSERT DATA BARU ===")
buku.insert("BK045", "Mein Kampf")
buku.insert("BK111", "Bumi Manusia")     
buku.display()

# search
print("\n=== SEARCH ===")
buku.search("BK111")
buku.search("BK077")

# delete
print("\n=== DELETE ===")
buku.delete("BK222")
buku.display()


    
    
