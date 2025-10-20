from OrangCilok import OrangCilok

class PenggemarCilok(OrangCilok):
    def __init__(self, no_ktp, nama, alamat, list_pedagang_cilok=None, list_cilok_favorite=None):
        super().__init__(no_ktp, nama, alamat)
        self.list_pedagang_cilok = list_pedagang_cilok if list_pedagang_cilok else []
        self.list_cilok_favorite = list_cilok_favorite if list_cilok_favorite else []

    # Setter dan Getter
    def set_list_pedagang_cilok(self, daftar): self.list_pedagang_cilok = daftar
    def get_list_pedagang_cilok(self): return self.list_pedagang_cilok

    def set_list_cilok_favorite(self, daftar): self.list_cilok_favorite = daftar
    def get_list_cilok_favorite(self): return self.list_cilok_favorite

    # Print
    def print_penggemar(self, prefix=""):
        print(f"{prefix}[Penggemar Cilok]")
        print(f"{prefix}Nama: {self.nama}")
        print(f"{prefix}Favorit: {self.list_cilok_favorite}")
        print(f"{prefix}Pedagang langganan: {self.list_pedagang_cilok}")
