class Node:
  def __init__(self, id_buku, judul ):
    self.id = id_buku
    self.judul = judul
    self.left = None
    self.right = None

class BST:
  def __init__(self):
    self.root = None

  def insert(self, id_buku, judul):
    def _insert(node, id_buku, judul):
      if node is None:
       return Node(id_buku, judul)
    
      if id_buku < node.id:
        node.left = _insert(node.left, id_buku, judul)
      elif id_buku > node.id:
        node.right = _insert(node.right, id_buku, judul)
      return node
    
    self.root = _insert(self.root, id_buku, judul)
    print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
    
  def search(self, id_buku):
    def _search(node):
        if node is None:
            return None
        elif node.id == id_buku:
            return node
        elif id_buku < node.id:
            return _search(node.left)
        else:
            return _search(node.right)
        
    return _search(self.root)
        
  def traversal_inorder(self):
      print("\n[INFO] Koleksi Buku (In-Order Traversal):")
      nomor = [1] 
      def _traversal_inorder(node):
        if node is None:
            return
        _traversal_inorder(node.left)
        print(f"{nomor[0]}. {node.id} - {node.judul}")
        nomor[0] += 1
        _traversal_inorder(node.right)

      _traversal_inorder(self.root)

  def get_min(self):
    node = self.root
    while node.left:
        node = node.left
    return node
  
  def get_max(self):
    node = self.root
    while node.right:
        node = node.right
    return node
  
  def height(self):
    def _height(node):
        if node is None:
            return -1  
        return 1 + max(_height(node.left), _height(node.right))

    return _height(self.root)

print("SISTEM KATALOG PERPUSTAKAAN 'ILMU TERANG'")
print("=========================================")

bst = BST()

# 1. input data
bst.insert(50, "Dasar Pemrograman")
bst.insert(30, "Struktur Data")
bst.insert(70, "Kecerdasan Buatan")
bst.insert(20, "Matematika Diskrit")
bst.insert(40, "Basis Data")
bst.insert(60, "Jaringan Komputer")
bst.insert(80, "Sistem Operasi")

# 2. cek koleksi
bst.traversal_inorder()

# 3. pencarian
hasil = bst.search(60)
if hasil:
    print(f"\n[SEARCH] Mencari ID 60... Ditemukan! Judul: {hasil.judul}")
else:
    print("[SEARCH] Mencari ID 60... Data tidak ditemukan.")

hasil = bst.search(100)
if hasil:
    print(f"[SEARCH] Mencari ID 100... Ditemukan! Judul: {hasil.judul}")
else:
    print("[SEARCH] Mencari ID 100... Data tidak ditemukan.")

min_buku = bst.get_min()
max_buku = bst.get_max()

# 4. statistik
print(f"\n[STATISTIK] ID Terkecil: {min_buku.id}")
print(f"[STATISTIK] ID Terbesar: {max_buku.id}")

# 5. analisis struktur
print(f"[INFO] Tinggi (Height) Tree: {bst.height()}")

print("=========================================")
print("Simulasi Selesai!")


  

  

