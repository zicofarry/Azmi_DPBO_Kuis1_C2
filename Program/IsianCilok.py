class IsianCilok:
    def __init__(self, kode_bahan, nama_isian, status):
        self.kode_bahan = kode_bahan
        self.nama_isian = nama_isian
        self.status = status  # vegetarian/non-vegetarian

    # Setter dan Getter
    def set_kode_bahan(self, kode): self.kode_bahan = kode
    def get_kode_bahan(self): return self.kode_bahan

    def set_nama_isian(self, nama): self.nama_isian = nama
    def get_nama_isian(self): return self.nama_isian

    def set_status(self, status): self.status = status
    def get_status(self): return self.status

    # Print
    def print_isian(self, prefix=""):
        print(f"{prefix}[Isian Cilok]")
        print(f"{prefix}Nama Isian: {self.nama_isian}")
        print(f"{prefix}Status: {self.status}")
