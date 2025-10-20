from OrangCilok import OrangCilok

class PedagangCilok(OrangCilok):
    def __init__(self, no_ktp, nama, alamat, tahun_awal_dagang, jenis, list_cilok_dijual=None):
        super().__init__(no_ktp, nama, alamat)
        self.tahun_awal_dagang = tahun_awal_dagang
        self.jenis = jenis
        self.list_cilok_dijual = list_cilok_dijual if list_cilok_dijual else []

    # Setter dan Getter
    def set_tahun_awal_dagang(self, tahun): self.tahun_awal_dagang = tahun
    def get_tahun_awal_dagang(self): return self.tahun_awal_dagang

    def set_jenis(self, jenis): self.jenis = jenis
    def get_jenis(self): return self.jenis

    def set_list_cilok_dijual(self, daftar): self.list_cilok_dijual = daftar
    def get_list_cilok_dijual(self): return self.list_cilok_dijual

    # Print
    def print_pedagang(self, prefix=""):
        print(f"{prefix}[Pedagang Cilok]")
        print(f"{prefix}Tahun Awal Dagang: {self.tahun_awal_dagang}")
        print(f"{prefix}Jenis: {self.jenis}")
        print(f"{prefix}Jual: {self.list_cilok_dijual}")
