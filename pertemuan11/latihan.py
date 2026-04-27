class Node:
    def _init_(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None

class Queue:
    def _init_(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, nama, keluhan):
        new_node = Node(nama, keluhan)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.length += 1
        print(f"[DAFTAR] {nama} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self.length})")

    def dequeue(self):
        if self.is_empty():
            print("[KOSONG] Tidak ada pasien.")
            return None

        temp = self.front
        self.front = temp.next
        self.length -= 1

        if self.front is None:
            self.rear = None

        print(f"[PANGGIL] Dokter memanggil: {temp.nama} (keluhan: {temp.keluhan})")
        return temp

    def peek(self):
        if self.is_empty():
            print("[PEEK] Antrian kosong.")
            return None

        print(f"[PEEK] Pasien berikutnya: {self.front.nama} - {self.front.keluhan}")
        return self.front

    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length

    def clear(self):
        self.front = None
        self.rear = None
        self.length = 0
        print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan")

    def printQueue(self):
        if self.is_empty():
            print("[ANTRIAN] kosong")
            return

        print("\n[ANTRIAN SAAT INI]")
        current = self.front
        i = 1
        while current:
            print(f"{i}. {current.nama} -> {current.keluhan}")
            current = current.next
            i += 1

antrian = Queue()

print("====================================")
print(" SISTEM ANTRIAN POLI UMUM")
print(" RS Sehat Bersama")
print("====================================\n")
print("[CEK] Apakah antrian kosong? →", "YA, antrian masih kosong." if antrian.is_empty() else "TIDAK")
antrian.enqueue("BUDI", "demam tinggi")
antrian.enqueue("ANI", "batuk pilek")
antrian.enqueue("CITRA", "sakit kepala")
print(f"\n[INFO] Jumlah pasien menunggu: {antrian.size()} orang")
antrian.peek()
antrian.dequeue()
antrian.enqueue("DODI", "nyeri perut")
antrian.printQueue()
antrian.dequeue()
print(f"\n[INFO] Jumlah pasien masih menunggu: {antrian.size()} orang")
antrian.clear()
print("[CEK] Apakah antrian kosong? →", "YA, antrian sudah kosong." if antrian.is_empty() else "TIDAK")
print("\n====================================")
print(" Simulasi Selesai!")
print("====================================")