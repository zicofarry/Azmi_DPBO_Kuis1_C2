class KategoriStandarEkspor:
    def __init__(self, kode_standar, nama_standar, level):
        self.kode_standar = kode_standar
        self.nama_standar = nama_standar
        self.level = level

    # Setter dan Getter
    def set_kode_standar(self, kode): self.kode_standar = kode
    def get_kode_standar(self): return self.kode_standar

    def set_nama_standar(self, nama): self.nama_standar = nama
    def get_nama_standar(self): return self.nama_standar

    def set_level(self, level): self.level = level
    def get_level(self): return self.level

    # Print
    def print_kategori(self, prefix=""):
        print(f"{prefix}[Kategori Ekspor] {self.nama_standar} (Kode: {self.kode_standar}), Level: {self.level}")
