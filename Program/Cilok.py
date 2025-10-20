class Cilok:
    def __init__(self, kode_cilok, nama, isian, harga, berat):
        self.kode_cilok = kode_cilok
        self.nama = nama
        self.isian = isian
        self.harga = harga
        self.berat = berat

    # Setter dan Getter
    def set_kode_cilok(self, kode): self.kode_cilok = kode
    def get_kode_cilok(self): return self.kode_cilok

    def set_nama(self, nama): self.nama = nama
    def get_nama(self): return self.nama

    def set_isian(self, isian): self.isian = isian
    def get_isian(self): return self.isian

    def set_harga(self, harga): self.harga = harga
    def get_harga(self): return self.harga

    def set_berat(self, berat): self.berat = berat
    def get_berat(self): return self.berat

    # Print
    def print_cilok(self, prefix=""):
        print(f"{prefix}[Cilok]")
        print(f"{prefix}Nama: {self.nama}")
        print(f"{prefix}Harga: {self.harga}")
        print(f"{prefix}Berat: {self.berat} gram")
        print(f"{prefix}{prefix}Nama Isian: {self.isian}")
