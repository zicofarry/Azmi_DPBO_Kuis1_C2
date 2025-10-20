class TempatJualCilok:
    def __init__(self, kode_tempat, nama, list_alamat=None, jaringan="offline"):
        self.kode_tempat = kode_tempat
        self.nama = nama
        self.list_alamat = list_alamat if list_alamat else []
        self.jaringan = jaringan

    # Setter dan Getter
    def set_kode_tempat(self, kode): self.kode_tempat = kode
    def get_kode_tempat(self): return self.kode_tempat

    def set_nama(self, nama): self.nama = nama
    def get_nama(self): return self.nama

    def set_list_alamat(self, daftar): self.list_alamat = daftar
    def get_list_alamat(self): return self.list_alamat

    def set_jaringan(self, jaringan): self.jaringan = jaringan
    def get_jaringan(self): return self.jaringan

    # Print
    def print_tempat(self, prefix=""):
        print(f"{prefix}[Tempat Jual Cilok]")
        print(f"{prefix}Kode: {self.kode_tempat}")
        print(f"{prefix}Nama: {self.nama}")
        print(f"{prefix}Jaringan: {self.jaringan}")
        print(f"{prefix}Alamat: {self.list_alamat}")
