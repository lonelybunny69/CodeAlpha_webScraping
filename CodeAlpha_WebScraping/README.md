# 🕷️ CodeAlpha Internship — Task 1: Web Scraping

Proyek ini merupakan bagian dari program **CodeAlpha Internship** (Web Scraping Task).
Script Python ini melakukan web scraping pada situs **[books.toscrape.com](http://books.toscrape.com/)** — sebuah website dummy yang memang dirancang untuk latihan web scraping.

---

## 📋 Fitur

- ✅ Scraping **semua 50 halaman** (~1000 buku) secara otomatis
- ✅ Mengambil data: **Judul**, **Harga**, **Rating**, dan **Status Stok**
- ✅ Membersihkan data (harga dikonversi ke float, rating ke angka 1–5)
- ✅ Error handling jika halaman gagal diakses
- ✅ Hasil disimpan ke file **CSV** yang bisa dibuka di Excel
- ✅ Data diurutkan berdasarkan **rating tertinggi**

---

## 🛠️ Teknologi yang Digunakan

| Library       | Fungsi                                      |
|---------------|---------------------------------------------|
| `requests`    | Mengunduh konten halaman web (HTTP request) |
| `BeautifulSoup` | Mem-parsing/membaca struktur HTML         |
| `pandas`      | Mengolah data dan menyimpan ke CSV          |
| `time`        | Memberi jeda antar request (etis scraping)  |

---

## 🚀 Cara Menjalankan

### 1. Clone repository

```bash
git clone https://github.com/lonelybunny69/CodeAlpha_webScraping.git
cd CodeAlpha_webScraping
```

### 2. Install dependencies

```bash
pip install requests beautifulsoup4 pandas
```

### 3. Jalankan script

```bash
python Task1.py
```

---

## 📁 Output

Setelah script selesai berjalan, akan muncul file `scraping_book.csv` di folder yang sama. File ini berisi data semua buku dengan kolom:

| Kolom          | Deskripsi                           |
|----------------|-------------------------------------|
| `Judul`        | Judul buku                          |
| `Harga (£)`    | Harga dalam Pound Sterling (float)  |
| `Rating (1-5)` | Rating bintang dalam angka (1–5)    |
| `Stok`         | Status ketersediaan buku            |

---

## 📊 Contoh Output

```
Judul                                          Harga (£)  Rating (1-5)  Stok
It's Only the Himalayas                            45.17             5  In stock
Full Moon over Noah's Ark                          49.43             5  In stock
...
```

---

## 👤 Author

**Nama:** [Nama Kamu]  
**Program:** CodeAlpha Internship — Web Scraping Task  
**Website Target:** [books.toscrape.com](http://books.toscrape.com/)
