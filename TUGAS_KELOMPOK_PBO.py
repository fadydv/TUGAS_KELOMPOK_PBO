#srp
# anti-pattern
class SistemPerpustakaan:
    def __init__(self, nama, isbn, stok):
        self.nama = nama
        self.isbn = isbn
        self.stok = stok

    def cari_buku(self, keyword):
        return f"Mencari: {keyword}"

    def cetak_label(self):
        return f"Label: {self.isbn}"

    def kirim_notifikasi(self, email):
        pass  # SMTP logic

    def simpan_ke_db(self):
        pass  # SQL logic

    def buat_laporan_pdf(self):
        pass  # PDF logic
        
#pattern
class Buku:
    def __init__(self, nama, isbn, stok):
        self.nama = nama
        self.isbn = isbn
        self.stok = stok

class KatalogBuku:
    def cari(self, keyword: str) -> list:
        return []  # logic pencarian

class PencetakLabel:
    def cetak(self, buku: Buku) -> str:
        return f"Label: {buku.isbn}"

class NotifikasiEmail:
    def kirim(self, email: str, pesan: str):
        pass  # SMTP logic

class RepositoriBuku:
    def simpan(self, buku: Buku):
        pass  # SQL logic

#ocp
#anti-pattern
class KalkulatorDiskon:
    def hitung(self, harga, tipe_member):
        if tipe_member == "reguler":
            return harga * 0.95
        elif tipe_member == "silver":
            return harga * 0.90
        elif tipe_member == "gold":
            return harga * 0.80
        elif tipe_member == "platinum":
            return harga * 0.70
        #untuk menambah member diamond harus masuk ke sini dan mengubah method lagi

#pattern
from abc import ABC, abstractmethod

class StrategiDiskon(ABC):
    @abstractmethod
    def hitung(self, harga: float) -> float: ...

class DiskonReguler(StrategiDiskon):
    def hitung(self, harga): return harga * 0.95

class DiskonSilver(StrategiDiskon):
    def hitung(self, harga): return harga * 0.90

class DiskonGold(StrategiDiskon):
    def hitung(self, harga): return harga * 0.80

# tambah member diamond hanya tniggal membuat class baru
class DiskonDiamond(StrategiDiskon):
    def hitung(self, harga): return harga * 0.60

class KalkulatorDiskon:
    def __init__(self, strategi: StrategiDiskon):
        self.strategi = strategi
    def hitung(self, harga):
        return self.strategi.hitung(harga)

#lsp
#anti-pattern


#pattern