
# Tugas Pemrograman Berbasis Objek / OOP
**Materi SOLID**

## Anggota Kelompok :
* **Devon Falen Pasae | 2409106055**
* **Inayah Ramadhani | 2409106068**
* **Andi Nurfadillah Hasan | 2409106087**
* **Nadia Rahmah | 2409106018**


# 🏛️ SOLID Principles — Panduan dengan Contoh Python

README ini menjelaskan lima prinsip **SOLID** dalam pemrograman berorientasi objek, lengkap dengan contoh kode anti-pattern dan solusinya dalam bahasa Python.

---

## Daftar Isi

- [SRP — Single Responsibility Principle](#srp--single-responsibility-principle)
- [OCP — Open/Closed Principle](#ocp--openclosed-principle)
- [LSP — Liskov Substitution Principle](#lsp--liskov-substitution-principle)
- [ISP — Interface Segregation Principle](#isp--interface-segregation-principle)
- [DIP — Dependency Inversion Principle](#dip--dependency-inversion-principle)

---

## SRP — Single Responsibility Principle

> **"Sebuah class hanya boleh punya satu alasan untuk berubah."**

### ❌ Anti-Pattern

```python
class SistemPerpustakaan:
    def __init__(self, nama, isbn, stok): ...
    def cari_buku(self, keyword): ...
    def cetak_label(self): ...
    def kirim_notifikasi(self, email): ...
    def simpan_ke_db(self): ...
    def buat_laporan_pdf(self): ...
```

**Masalah:** Satu class menanggung terlalu banyak tanggung jawab — data buku, pencarian, label, notifikasi, database, dan laporan. Jika logika email berubah, class ini harus disentuh meski perubahan tidak ada kaitannya dengan buku.

### ✅ Pattern yang Benar

```python
class Buku:                  # hanya menyimpan data buku
class KatalogBuku:           # hanya menangani pencarian
class PencetakLabel:         # hanya mencetak label
class NotifikasiEmail:       # hanya mengirim email
class RepositoriBuku:        # hanya berinteraksi dengan database
```

**Keuntungan:** Setiap class fokus pada satu pekerjaan. Mudah diuji, dimodifikasi, dan diganti tanpa mempengaruhi bagian lain.

---

## OCP — Open/Closed Principle

> **"Class terbuka untuk ekstensi, tertutup untuk modifikasi."**

### ❌ Anti-Pattern

```python
class KalkulatorDiskon:
    def hitung(self, harga, tipe_member):
        if tipe_member == "reguler": return harga * 0.95
        elif tipe_member == "silver": return harga * 0.90
        elif tipe_member == "gold":   return harga * 0.80
        # untuk menambah tipe member baru, harus mengubah method
```

**Masalah:** Setiap kali ada tipe member baru, kode lama harus dimodifikasi — berisiko memunculkan bug pada logika yang sudah berjalan.

### ✅ Pattern yang Benar

```python
class StrategiDiskon(ABC):
    @abstractmethod
    def hitung(self, harga: float) -> float: ...

class DiskonReguler(StrategiDiskon):
    def hitung(self, harga): return harga * 0.95

class DiskonDiamond(StrategiDiskon):   # tambah member baru = class baru
    def hitung(self, harga): return harga * 0.60

class KalkulatorDiskon:
    def __init__(self, strategi: StrategiDiskon):
        self.strategi = strategi
```

**Keuntungan:** Menambah tipe member baru cukup dengan membuat class baru — tanpa menyentuh kode yang sudah ada.

---

## LSP — Liskov Substitution Principle

> **"Subclass harus bisa menggantikan superclass-nya tanpa merusak program."**

### ❌ Anti-Pattern

```python
class Kendaraan:
    def isi_bbm(self, liter): ...

class MobilListrik(Kendaraan):
    def isi_bbm(self, liter):
        raise NotImplementedError("Mobil listrik tidak isi BBM")

def perjalanan(kendaraan: Kendaraan):
    kendaraan.isi_bbm(40)   # CRASH jika dapat MobilListrik!
```

**Masalah:** `MobilListrik` tidak bisa menggantikan `Kendaraan` secara utuh karena method `isi_bbm` justru melempar error — melanggar kontrak yang dijanjikan superclass.

### ✅ Pattern yang Benar

```python
class Kendaraan(ABC):
    @abstractmethod
    def nyalakan_mesin(self) -> str: ...
    @abstractmethod
    def isi_energi(self, jumlah: float) -> str: ...

class KendaraanBBM(Kendaraan):
    def isi_energi(self, liter): return f"Isi {liter}L bensin"

class KendaraanListrik(Kendaraan):
    def isi_energi(self, kwh): return f"Charge {kwh} kWh"

def perjalanan(kendaraan: Kendaraan):
    kendaraan.isi_energi(40)   # aman untuk semua subclass
```

**Keuntungan:** Semua subclass memiliki kontrak yang sama (`isi_energi`), sehingga bisa disubstitusi tanpa risiko crash.

---

## ISP — Interface Segregation Principle

> **"Class tidak boleh dipaksa mengimplementasikan method yang tidak ia butuhkan."**

### ❌ Anti-Pattern

```python
class PegawaiToko(ABC):
    def jual_produk(self): ...
    def atur_stok(self): ...
    def buat_laporan(self): ...
    def kelola_keuangan(self): ...
    def rekrut_karyawan(self): ...

class Kasir(PegawaiToko):
    def jual_produk(self): return "Transaksi"
    def atur_stok(self): raise NotImplementedError("Bukan tugasku!")
    def rekrut_karyawan(self): raise NotImplementedError("Bukan tugasku!")
    # ... dan seterusnya
```

**Masalah:** `Kasir` dipaksa mewarisi method yang tidak relevan, menghasilkan implementasi palsu berisi `raise NotImplementedError`.

### ✅ Pattern yang Benar

```python
class BisaPenjualan(ABC):
    @abstractmethod
    def jual_produk(self): ...

class BisaLaporan(ABC):
    @abstractmethod
    def buat_laporan(self): ...

class Kasir(BisaPenjualan):             # hanya yang relevan
    def jual_produk(self): return "Transaksi!"

class Manager(BisaLaporan, BisaRekrut): # kombinasi sesuai kebutuhan
    def buat_laporan(self): return "Laporan Q4"
    def rekrut_karyawan(self): return "Hiring!"
```

**Keuntungan:** Setiap class hanya mewarisi interface yang benar-benar dibutuhkan, membuat kode lebih bersih dan mudah dipahami.

---

## DIP — Dependency Inversion Principle

> **"Class tingkat tinggi tidak boleh bergantung pada class tingkat rendah — keduanya harus bergantung pada abstraksi."**

### ❌ Anti-Pattern

```python
class LayananProduk:
    def __init__(self):
        self.db = DatabaseSQLite()   # terikat langsung ke SQLite!

    def tambah_produk(self, nama, harga):
        self.db.simpan({"nama": nama, "harga": harga})
```

**Masalah:** `LayananProduk` terikat keras ke `DatabaseSQLite`. Ingin ganti ke PostgreSQL? Kode bisnis harus diubah.

### ✅ Pattern yang Benar

```python
class StorageProduk(ABC):
    @abstractmethod
    def simpan(self, data: dict): ...

class StorageSQLite(StorageProduk):   # implementasi konkret
    def simpan(self, data): ...       # SQLite logic

class StoragePostgres(StorageProduk): # implementasi lain
    def simpan(self, data): ...       # PostgreSQL logic

class LayananProduk:
    def __init__(self, storage: StorageProduk):
        self.storage = storage        # terima abstraksi, bukan konkret!

# Ganti database = tinggal ganti injeksi
svc = LayananProduk(StoragePostgres())
```

**Keuntungan:** `LayananProduk` tidak peduli database apa yang digunakan. Ganti implementasi storage semudah mengganti satu baris kode di titik injeksi.

