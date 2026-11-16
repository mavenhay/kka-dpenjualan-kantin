# D. Lembar Perencanaan Proyek Kelompok (Project Charter)

## 1. Nama Anggota Kelompok
**Anggota 1:** Atha Khoirun Ayyasi  
**Anggota 2:** Maven Helios Agathon Yesstian

## 2. Dataset yang Dipilih
- [o] Data Penjualan Kantin/Toko
- [ ] Data Nilai Akademik Siswa
- [ ] Data Sensor IoT Sederhana
- [ ] Dataset lain: ..............................................................

## 3. Pertanyaan Analisis Awal
1. Apa produk yang terlaris?
2. Apa produk yang termurah?
3. Apakah ada data yang nilainya tidak wajar?

## 4. Dugaan Masalah Kualitas Data
- [o] Missing value pada kolom: jumlah_terjual, nama_kasir & harga_satuan
- [0] Duplikat data
- [0] Tipe data tidak sesuai pada kolom: harga_satuan, jumlah_terjual
- [ ] Lainnya: ......................................................................

## 5. Rencana Teknik Pembersihan Data
-Missing value dihapus/diisi
-duplikat data dihapus duplikatnya
-menjadikan 1 tipe data yang sama, tiap kolom

## 6. Rencana Manipulasi Data
- **Filter:** Hanya menampilkan transaksi dengan metode pembayaran QRIS, atau transaksi untuk produk Jus Alpukat.
- **Sort:** Mengurutkan transaksi berdasarkan Tanggal dari yang terbaru ke terlama, atau berdasarkan Total Harga terbanyak.
- **Kolom Turunan:** Membuat kolom Total Pendapatan dari hasil perkalian Jumlah Beli * Harga Satuan, atau mengekstrak Hari dari kolom Tanggal.
- **GroupBy/Agregasi:** Mengelompokkan data berdasarkan Penjual (Bu Wati) untuk melihat total pendapatan bulanan, atau mengelompokkan berdasarkan Kategori (MINUMAN) untuk menghitung total unit yang terjual.

## 7. Jadwal Kerja
- **P3 (Loading & Inspection):** 
-Load dataset "dataset_penjualan_kantin.csv" ke dalam program (misalnya menggunakan library pandas).
-Melakukan pemeriksaan awal struktur data (mengecek jumlah baris/kolom, nama kolom, serta tipe data awal).
-Mengidentifikasi masalah kualitas data seperti missing value dan duplikat.

- **P4 (Cleaning):** 
-Membersihkan data bermasalah: menghapus/mengisi nilai yang hilang (missing value) pada kolom jumlah_terjual dan harga_satuan.
-Menghapus baris data yang duplikat.
-Memperbaiki dan menyamakan tipe data kolom (misalnya mengubah tipe data harga_satuan agar sesuai).

- **P5 (Manipulation):**
-filtering dan sorting data sesuai kebutuhan analisis.
-Membuat kolom turunan (derived column), seperti Total Pendapatan (jumlah_terjual * harga_satuan) atau mengekstrak Hari dari tanggal.
-Melakukan agregasi (GroupBy) untuk melihat ringkasan penjualan berdasarkan Penjual atau Kategori Produk.

- **P6 (Uji & Presentasi):** 
-Menguji ulang keseluruhan kode program agar berjalan tanpa eror.
-Menyusun kesimpulan/wawasan (insight) dari hasil analisis data.
-Mempersiapkan bahan presentasi dan mempresentasikan hasil proyek kelompok.

## 8. Pembagian Peran
- **Anggota 1 (Maven):** P3 - P4
- **Anggota 2 (Atha):** P5 - P6