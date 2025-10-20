class LevelKategori:
    def __init__(self, jenis_level, nilai):
        self.jenis_level = jenis_level
        self.nilai = nilai

    # Setter dan Getter
    def set_jenis_level(self, jenis): self.jenis_level = jenis
    def get_jenis_level(self): return self.jenis_level

    def set_nilai(self, nilai): self.nilai = nilai
    def get_nilai(self): return self.nilai

    # Print
    def print_level(self, prefix=""):
        print(f"{prefix}[Level Kategori] {self.jenis_level} - Nilai: {self.nilai}/10")
