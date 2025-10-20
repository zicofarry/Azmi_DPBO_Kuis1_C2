class EksportirCilok:
    def __init__(self, status_pedagang, list_negara_ekspor=None):
        self.status_pedagang = status_pedagang
        self.list_negara_ekspor = list_negara_ekspor if list_negara_ekspor else []

    # Setter dan Getter
    def set_status_pedagang(self, status): self.status_pedagang = status
    def get_status_pedagang(self): return self.status_pedagang

    def set_list_negara_ekspor(self, daftar): self.list_negara_ekspor = daftar
    def get_list_negara_ekspor(self): return self.list_negara_ekspor
