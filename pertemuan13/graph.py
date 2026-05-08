class Graph:
    def __init__(self):
        self.graph = {}

    def tambah_kota(self, nama):
        if nama not in self.graph:
            self.graph[nama] = []

    def tambah_jalan(self, u, v, jarak):
        self.tambah_kota(u)
        self.tambah_kota(v)
        self.graph[u].append((v, jarak))
        self.graph[v].append((u, jarak))

    def tampilkan_graph(self):
        print("\n[INFO] Struktur Jaringan Distribusi:")

        for kota in self.graph:
            print(f"- {kota} terhubung ke:", end=" ")

            tetangga = []

            for tujuan, jarak in self.graph[kota]:
                tetangga.append(f"{tujuan} ({jarak} km)")

            print(", ".join(tetangga))

    def dijkstra(self, kota_asal):
        jarak = {}

        for kota in self.graph:
            jarak[kota] = float('inf')

        jarak[kota_asal] = 0

        visited = []

        while len(visited) < len(self.graph):
            min_kota = None
            min_jarak = float('inf')

            for kota in self.graph:
                if kota not in visited and jarak[kota] < min_jarak:
                    min_jarak = jarak[kota]
                    min_kota = kota

            if min_kota is None:
                break

            visited.append(min_kota)

            for tetangga, bobot in self.graph[min_kota]:

                if tetangga not in visited:
                    jarak_baru = jarak[min_kota] + bobot

                    if jarak_baru < jarak[tetangga]:
                        jarak[tetangga] = jarak_baru

        print(f"\n[HASIL] Jarak Terpendek dari {kota_asal}:")

        nomor = 1
        for kota in jarak:
            if kota != kota_asal:
                print(f"{nomor}. Ke {kota}: {jarak[kota]} km")
                nomor += 1

print("SISTEM NAVIGASI LOGISTIK 'KILAT MAJU'")
print("=========================================")

navigasi = Graph()

# input
print(f"[INPUT] Menambahkan jalan: Jakarta - Bandung (150 km)")
navigasi.tambah_jalan("Jakarta", "Bandung", 150)

print(f"[INPUT] Menambahkan jalan: Jakarta - Cirebon (200 km)")
navigasi.tambah_jalan("Jakarta", "Cirebon", 200)

print(f"[INPUT] Menambahkan jalan: Bandung - Tasikmalaya (100 km)")
navigasi.tambah_jalan("Bandung", "Tasikmalaya", 100)

print(f"[INPUT] Menambahkan jalan: Bandung - Cirebon (130 km)")
navigasi.tambah_jalan("Bandung", "Cirebon", 130)

print(f"[INPUT] Menambahkan jalan: Cirebon - Semarang (250 km)")
navigasi.tambah_jalan("Cirebon", "Semarang", 250)

print(f"[INPUT] Menambahkan jalan: Tasikmalaya - Semarang (200 km)")
navigasi.tambah_jalan("Tasikmalaya", "Semarang", 200)

# tampilkan graph
navigasi.tampilkan_graph()

# dijkstra
print("\n[PROSES] Menghitung rute terpendek dari: Jakarta...")
navigasi.dijkstra("Jakarta")

print("\n=========================================")
print("Simulasi Navigasi Selesai!")