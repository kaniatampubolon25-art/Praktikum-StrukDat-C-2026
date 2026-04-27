#Soal 1
print("\nSoal 1")

class Node:
    def __init__(self, plat):
        self.plat = plat 
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_kendaraan(self,plat):
        new_node = Node(plat)

        if not self.head:
           self.head = new_node
           self.tail = new_node
        else:
           new_node.prev = self.tail
           self.tail.next = new_node
           self.tail = new_node

    def tampilkan_maju(self):
        print("[Maju]")
        current = self.head
        while current:
            print(current.plat)
            current = current.next

    def tampilkan_mundur(self):
        print("\n[Mundur]")
        current = self.tail
        while current:
            print(current.plat)
            current = current.prev

parkir = DoubleLinkedList()

parkir.tambah_kendaraan("B 1234 ABC")
parkir.tambah_kendaraan("D 5678 XYZ")
parkir.tambah_kendaraan("A 9999 TUV")
parkir.tampilkan_maju()
parkir.tampilkan_mundur()

#soal 2
print("\nSoal 2")

class Node:
    def __init__(self, plat):
        self.plat = plat 
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_kendaraan(self,plat):
        new_node = Node(plat)

        if not self.head:
           self.head = new_node
           self.tail = new_node
        else:
           new_node.prev = self.tail
           self.tail.next = new_node
           self.tail = new_node

    def tampilkan_maju(self):
        current = self.head
        while current:
            print(current.plat)
            current = current.next

    def tampilkan_mundur(self):
        current = self.tail
        while current:
            print(current.plat)
            current = current.prev

    def hapus_kendaraan(self,plat):
        hapus = self.head

        while hapus:
            if hapus.plat == plat:

                # jika head
                if hapus.prev is None:
                    self.head = hapus.next
                    if self.head:
                        self.head.prev = None

                # jika tail
                elif hapus.next is None:
                    self.tail = hapus.prev
                    self.tail.next = None

                # jika tengah
                else:
                    hapus.prev.next = hapus.next
                    hapus.next.prev = hapus.prev

                return

            hapus = hapus.next

        print(f"Kendaraan {plat} tidak ditemukan")
    
parkir = DoubleLinkedList()

parkir.tambah_kendaraan("B 1111 AA")
parkir.tambah_kendaraan("D 2222 BB")
parkir.tambah_kendaraan("A 3333 CC")
parkir.tambah_kendaraan("B 4444 DD")

print("Sebelum:")
parkir.tampilkan_maju()

parkir.hapus_kendaraan("A 3333 CC")

print("\nSesudah:")
parkir.tampilkan_maju()

#soal 3
print("\nSoal 3")

class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_petugas(self, nama):
        new_node = Node(nama)

        if not self.head:
            self.head = self.tail = new_node
            self.tail.next = self.head  
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head  

    def giliran_berikutnya(self, n):
        if not self.head:
            print("Tidak ada petugas")
            return

        current = self.head

        for i in range(1, n+1):
            print(f"Giliran {i}: {current.nama}")
            current = current.next

valet = CircularLinkedList()

valet.tambah_petugas("Andi")
valet.tambah_petugas("Budi")
valet.tambah_petugas("Citra")
valet.tambah_petugas("Dewi")
valet.giliran_berikutnya(6)
    










   
   
   


      





