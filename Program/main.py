from OrangCilok import OrangCilok
from PedagangCilok import PedagangCilok
from PenggemarCilok import PenggemarCilok
from TempatJualCilok import TempatJualCilok
from Cilok import Cilok
from IsianCilok import IsianCilok
from EksportirCilok import EksportirCilok
from NegaraEksporCilok import NegaraEksporCilok
from KategoriStandarEkspor import KategoriStandarEkspor
from LevelKategori import LevelKategori

def main():

    # === IsianCilok (2 data) ===
    isian1 = IsianCilok("B001", "Ayam", "non-vegetarian")
    isian2 = IsianCilok("B002", "Keju", "vegetarian")
    isian3 = IsianCilok("B003", "Sapi", "non-vegetarian")

    # === Cilok (2 data) ===
    cilok1 = Cilok("C01", "Cilok Ayam", isian1.get_nama_isian(), 5000, 50)
    cilok2 = Cilok("C02", "Cilok Keju", isian2.get_nama_isian(), 6000, 55)
    cilok3 = Cilok("C03", "Cilok Sapi", isian3.get_nama_isian(), 7000, 60)

    # === PedagangCilok (2 data) ===
    pedagang1 = PedagangCilok("123", "Pak Ujang", "Bandung", 2010, "Produksi dan Jual", [cilok1.get_nama(), cilok2.get_nama()])
    pedagang2 = PedagangCilok("124", "Bu Euis", "Garut", 2015, "Reseller", [cilok3.get_nama()])

    # === PenggemarCilok (2 data) ===
    penggemar1 = PenggemarCilok("456", "Rina", "Jakarta", [pedagang1.get_nama()], [cilok2.get_nama()])
    penggemar2 = PenggemarCilok("457", "Budi", "Bekasi", [pedagang2.get_nama()], [cilok3.get_nama()])

    # === TempatJualCilok (2 data) ===
    tempat1 = TempatJualCilok("T01", "Warung Cilok Mang Ujang", ["Jl. Sukajadi No.1"], "offline")
    tempat2 = TempatJualCilok("T02", "Cilok Online Bu Euis", ["Jl. Ahmad Yani No.5"], "online")

    # === LevelKategori (2 data) ===
    level1 = LevelKategori("Premium", 9)
    level2 = LevelKategori("Standar", 7)

    # === KategoriStandarEkspor (2 data) ===
    kategori1 = KategoriStandarEkspor("K01", "Medium", level1.get_jenis_level())
    kategori2 = KategoriStandarEkspor("K02", "High", level2.get_jenis_level())

    # === NegaraEksporCilok (2 data) ===
    negara1 = NegaraEksporCilok("ID", "Indonesia", kategori1.get_nama_standar())
    negara2 = NegaraEksporCilok("MY", "Malaysia", kategori2.get_nama_standar())

    # === EksportirCilok (2 data) ===
    eksportir1 = EksportirCilok(True, [negara1.get_nama(), negara2.get_nama()])
    eksportir2 = EksportirCilok(False, [negara1.get_nama()])

    print("===== DATA CILOK =====")

    print("\n[Orang 1]")
    pedagang1.print_orang("   ")
    pedagang1.print_pedagang("      ")
    print("\n[Orang 2]")
    pedagang2.print_orang("   ")
    pedagang2.print_pedagang("      ")

    print("\n[Orang 3]")
    penggemar1.print_orang("   ")
    penggemar1.print_penggemar("      ")
    print("\n[Orang 4]")
    penggemar2.print_orang("   ")
    penggemar2.print_penggemar("      ")


    print("\n[Tempat Jual Cilok 1]")
    tempat1.print_tempat("  ")
    print("\n[Tempat Jual Cilok 2]")
    tempat2.print_tempat("  ")


    print("\n[Cilok 1]")
    cilok1.print_cilok("   ")
    print("\n[Cilok 2]")
    cilok2.print_cilok("   ")
    print("\n[Cilok 3]")
    cilok3.print_cilok("   ")

    print("[Isian Cilok]")
    isian1.print_isian("   ")
    isian2.print_isian("   ")
    isian3.print_isian("   ")

    
    print("\n[Eksportir Cilok]")
    print("  Status:", eksportir1.get_status_pedagang(), "| Negara:", eksportir1.get_list_negara_ekspor())
    print("  Status:", eksportir2.get_status_pedagang(), "| Negara:", eksportir2.get_list_negara_ekspor())

    print("\n[Negara Ekspor Cilok]")
    negara1.print_negara("   ")
    negara2.print_negara("   ")

    print("\n[Kategori Ekspor]")
    kategori1.print_kategori("   ")
    kategori2.print_kategori("   ")

    print("\n[Level Kategori]")
    level1.print_level("  ")
    level2.print_level("  ")

if __name__ == "__main__":
    main()
