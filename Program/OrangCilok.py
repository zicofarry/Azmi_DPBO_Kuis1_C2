class OrangCilok:
    def __init__(self, no_ktp, nama, alamat):
        self.no_ktp = no_ktp
        self.nama = nama
        self.alamat = alamat

    # Setter dan Getter
    def set_no_ktp(self, no_ktp): self.no_ktp = no_ktp
    def get_no_ktp(self): return self.no_ktp

    def set_nama(self, nama): self.nama = nama
    def get_nama(self): return self.nama

    def set_alamat(self, alamat): self.alamat = alamat
    def get_alamat(self): return self.alamat

    # Print
    def print_orang(self, prefix=""):
        print(f"{prefix}[Orang Cilok]")
        print(f"{prefix}KTP: {self.no_ktp}")
        print(f"{prefix}Nama: {self.nama}")
        print(f"{prefix}Alamat: {self.alamat}")
