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