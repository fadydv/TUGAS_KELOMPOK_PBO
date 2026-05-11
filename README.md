#  LAPORAN POSTTEST 4 - Detailing Kendaraan

## 1. Identitas 
* **Nama**        : Devon Falen Pasae
* **NIM**         : 2409106055
* **Sistem**      : Sistem Manajemen Detailing Kendaraan

---

## 2. Detail Program
Program ini merupakan pengembangan dari sistem sebelumnya yang kini mengimplementasikan prinsip Polimorfisme. Polimorfisme dalam OOP adalah konsep di mana sebuah class memiliki banyak "bentuk" method yang berbeda meskipun menggunakan nama yang sama.Pada pembaruan ini, program menerapkan dua jenis polimorfisme:Static Polymorphism (Overloading): Menggunakan nama method yang sama namun dengan parameter yang berbeda. Diterapkan pada fungsi pengaturan harga untuk membedakan antara harga normal dan harga diskon member.Dynamic Polymorphism (Overriding): Menggunakan pewarisan di mana subclass mendefinisikan ulang method milik superclass dengan nama dan parameter yang identik. Diterapkan pada penampilan data agar informasi yang keluar sesuai dengan jenis motor masing-masing.

---

## 3. Fitur Program
1. **Tambah Data / Create**: Menambahkan data transaksi.
2. **Daftar Data / Read**: Menampilkan data transaksi dengan format tabel.
3. **Edit Data / Update**: Mengubah detail transaksi.
4. **Hapus Data / Delete**: Menghapus data transaksi individual.
5. **Sistem Diskon (Polymorphism Statis)**: Secara otomatis menghitung harga berbeda jika pelanggan memiliki kartu member.
---

## 4. Output Program

- **Menu Utama**
<img src="POSTTEST_1/img_1.png" width="500">

- **Menu Tambah Data**
<img src="POSTTEST_1/img_2.png" width="500">

- **Menu Daftar Data**
<img src="POSTTEST_1/img_3.png" width="500">

- **Menu Edit Data**
<img src="POSTTEST_1/img_4.png" width="500">

- **Menu Hapus Data**
<img src="POSTTEST_1/img_5.png" width="500">

- **Opsi Keluar Program**
<img src="POSTTEST_1/img_6.png" width="500">

---

## 5. Struktur Class Baru

1. **Main.class**: Mengatur alur logika program dan interaksi pengguna (Looping & Switch-Case).

2. **Detailing.java (Superclass)**: Dasar dari semua objek detailing yang menyimpan data umum kendaraan motor.

3. **MotorMatic.java (Subclass)**: Spesialisasi untuk motor matic dengan tambahan atribut kapasitas bagasi.

4. **MotorSport.java (Subclass)**: Spesialisasi untuk motor sport dengan tambahan atribut kapasitas mesin (CC).

Struktur Class dengan Polymorphism
1. **Detailing.java (Superclass)**: Menerapkan Overloading pada method setHarga(). Satu versi untuk harga normal, satu versi lainnya menerima parameter double diskon.

2. **MotorMatic.java & MotorSport.java (Subclasses)**: Menerapkan Overriding pada method tampilkanBaris(). Method ini dipanggil pada saat runtime untuk menampilkan atribut unik (Bagasi/CC) secara seragam melalui referensi induk.

## 6. Dokumentasi Kode

**a. Implementasi Polymorphism Statis**
```java
public void setHarga(int harga) {
    this.harga = (harga < 0) ? 0 : harga;
}

public void setHarga(int harga, double diskon) {
    int totalDiskon = (int) (harga * diskon);
    this.harga = harga - totalDiskon;
}
```

**b. Implementasi Polymorphism Dinamis**
```java
@Override
public void tampilkanBaris(int no) {
    System.out.printf("| %-3d | %-15s | %-20s | Rp %-10d | Matic (Bagasi: %dL) |\n",
            no, merk, paket, harga, kapasitasBagasi);
}

@Override
public void tampilkanBaris(int no) {
    System.out.printf("| %-3d | %-15s | %-20s | Rp %-10d | Sport (Mesin: %dcc) |\n",
            no, merk, paket, harga, kapasitasMesin);
}
```

**c. Pemanggilan Polymorphism pada Program utama**
```java
if (isMember.equalsIgnoreCase("y")) {
    motorBaru.setHarga(hargaAwal, 0.1); // Menggunakan method dengan parameter diskon
} else {
    motorBaru.setHarga(hargaAwal);      // Menggunakan method dengan satu parameter
}

for (int i = 0; i < listData.size(); i++) {
    listData.get(i).tampilkanBaris(i + 1); // Memanggil method override secara otomatis
}
```

