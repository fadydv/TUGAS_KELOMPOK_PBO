# anti-pattern
class Lipstik:
    def __init__(self, merk, shade, harga):
        self.merk = merk
        self.shade = shade
        self.harga = harga

    def hitung_harga_diskon(self, persen):
        return self.harga - (self.harga * persen / 100)

    def simpan_ke_mysql(self):
        print(f"Menyimpan {self.merk} {self.shade} ke tabel lipstik")

    def cetak_label_harga(self):
        print(f"Produk: {self.merk}")
        print(f"Warna : {self.shade}")
        
#pattern
class Lipstik:
    def __init__(self, merk, shade, harga):
        self.merk = merk
        self.shade = shade
        self.harga = harga

class KalkulatorHarga:
    @staticmethod
    def diskon_promo(lipstik, persen):
        return lipstik.harga - (lipstik.harga * persen / 100)

class LipstikRepository:
    def simpan(self, lipstik):
        print(f"SQL: INSERT INTO lipstik VALUES ('{lipstik.merk}', '{lipstik.shade}')")

class PrinterKatalog:
    def cetak_katalog(self, lipstik):
        print(f"Menampilkan katalog: {lipstik.merk} - {lipstik.shade}")