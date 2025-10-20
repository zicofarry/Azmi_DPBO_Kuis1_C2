class NegaraEksporCilok:
    def __init__(self, kode_negara, nama, kategori_standar):
        self.kode_negara = kode_negara
        self.nama = nama
        self.kategori_standar = kategori_standar

    # Setter dan Getter
    def set_kode_negara(self, kode): self.kode_negara = kode
    def get_kode_negara(self): return self.kode_negara

    def set_nama(self, nama): self.nama = nama
    def get_nama(self): return self.nama

    def set_kategori_standar(self, kategori): self.kategori_standar = kategori
    def get_kategori_standar(self): return self.kategori_standar

    # Print
    def print_negara(self, prefix=""):
        print(f"{prefix}[Negara Ekspor] {self.nama} ({self.kode_negara}), Standar: {self.kategori_standar}")
