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
class Kendaraan:
    def isi_bbm(self, liter: float):
        return f"Isi {liter}L bensin"

    def nyalakan_mesin(self):
        return "Vroom!"

class MobilListrik(Kendaraan):
    def isi_bbm(self, liter):
        # EV tidak pakai BBM
        raise NotImplementedError(
            "Mobil listrik tidak isi BBM"
        )

# Kode ini crash jika dapat MobilListrik
def perjalanan(kendaraan: Kendaraan):
    kendaraan.isi_bbm(40)  # CRASH!
    kendaraan.nyalakan_mesin()

#pattern
from abc import ABC, abstractmethod

class Kendaraan(ABC):
    @abstractmethod
    def nyalakan_mesin(self) -> str: ...
    @abstractmethod
    def isi_energi(self, jumlah: float) -> str: ...

class KendaraanBBM(Kendaraan):
    def nyalakan_mesin(self): return "Vroom!"
    def isi_energi(self, liter):
        return f"Isi {liter}L bensin"

class KendaraanListrik(Kendaraan):
    def nyalakan_mesin(self): return "Siuuuu..."
    def isi_energi(self, kwh):
        return f"Charge {kwh} kWh"

# Aman, karena semua subclass punya isi_energi
def perjalanan(kendaraan: Kendaraan):
    kendaraan.isi_energi(40)  # tidak crash
    kendaraan.nyalakan_mesin()

#isp
#anti-pattern
class PegawaiToko(ABC):
    def jual_produk(self): ...
    def atur_stok(self): ...
    def buat_laporan(self): ...
    def kelola_keuangan(self): ...
    def rekrut_karyawan(self): ...

class Kasir(PegawaiToko):
    def jual_produk(self): return "Transaksi"
    def atur_stok(self):
        raise NotImplementedError("Kasir bukan gudang!")
    def buat_laporan(self):
        raise NotImplementedError("Kasir bukan manager!")
    def kelola_keuangan(self):
        raise NotImplementedError("Bukan HRD!")
    def rekrut_karyawan(self):
        raise NotImplementedError("Bukan HRD!")

#pattern
from abc import ABC, abstractmethod

class BisaPenjualan(ABC):
    @abstractmethod
    def jual_produk(self): ...

class BisaStok(ABC):
    @abstractmethod
    def atur_stok(self): ...

class BisaLaporan(ABC):
    @abstractmethod
    def buat_laporan(self): ...

class BisaRekrut(ABC):
    @abstractmethod
    def rekrut_karyawan(self): ...

# kasir hanya implement yang relevan
class Kasir(BisaPenjualan):
    def jual_produk(self): return "Transaksi!"

# manager implement semua yang diperlukan
class Manager(BisaLaporan, BisaRekrut):
    def buat_laporan(self): return "Laporan Q4"
    def rekrut_karyawan(self): return "Hiring!"

#dip
#anti pattern
import sqlite3

class DatabaseSQLite:
    def simpan(self, data):
        conn = sqlite3.connect("toko.db")
        # ... insert SQL ...

class LayananProduk:
    def __init__(self):
        self.db = DatabaseSQLite()

    def tambah_produk(self, nama, harga):
        self.db.simpan({"nama": nama, "harga": harga})

#pattern
from abc import ABC, abstractmethod

class StorageProduk(ABC):
    @abstractmethod
    def simpan(self, data: dict): ...

# Implementasi konkret
class StorageSQLite(StorageProduk):
    def simpan(self, data):
        pass  # SQLite logic

class StoragePostgres(StorageProduk):
    def simpan(self, data):
        pass  # PostgreSQL logic

class StorageMemori(StorageProduk): 
    def simpan(self, data): self.data = data

class LayananProduk:
    def __init__(self, storage: StorageProduk):
        self.storage = storage  # inject!

svc = LayananProduk(StoragePostgres())