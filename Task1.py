import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# ============================================================
# Web Scraping - Books to Scrape (books.toscrape.com)
# ============================================================

BASE_URL = "http://books.toscrape.com/"

RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/91.0.4472.124 Safari/537.36"
    )
}


def scrape_halaman(url):
    """
    Mengambil data semua buku dari satu halaman.
    Mengembalikan list of dict berisi data buku.
    """
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"  [WARN] Gagal mengakses {url}: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    buku_list = soup.find_all('article', class_='product_pod')

    data = []
    for buku in buku_list:
        judul = buku.h3.a['title']

        harga_raw = buku.find('p', class_='price_color').text
        harga = float(harga_raw.replace('Â£', '').replace('£', '').strip())

        stok = buku.find('p', class_='instock availability').text.strip()

        rating_class = buku.find('p', class_='star-rating')['class'][1]
        rating = RATING_MAP.get(rating_class, 0)

        data.append({
            'Judul': judul,
            'Harga (£)': harga,
            'Rating (1-5)': rating,
            'Stok': stok
        })

    return data


def get_next_page_url(soup, current_url):
    """
    Mencari URL halaman berikutnya dari tombol 'next'.
    Mengembalikan URL lengkap jika ada, atau None jika sudah halaman terakhir.
    """
    next_btn = soup.find('li', class_='next')
    if not next_btn:
        return None

    next_href = next_btn.a['href']

    if next_href.startswith('catalogue/'):
        return BASE_URL + next_href
    else:
        base = current_url.rsplit('/', 1)[0] + '/'
        return base + next_href


# ============================================================
# MAIN — Loop semua halaman
# ============================================================
print("[*] Memulai proses scraping books.toscrape.com...")
print("=" * 55)

semua_data = []
current_url = BASE_URL
halaman = 1

while current_url:
    print(f"  [Page {halaman}] Scraping: {current_url}")

    try:
        response = requests.get(current_url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"  [ERROR] Gagal mengakses halaman {halaman}: {e}")
        break

    soup = BeautifulSoup(response.text, 'html.parser')

    data_halaman = scrape_halaman(current_url)
    semua_data.extend(data_halaman)

    # Cari URL halaman berikutnya
    current_url = get_next_page_url(soup, current_url)
    halaman += 1

    time.sleep(0.5)

# ============================================================
# Simpan ke CSV
# ============================================================
df = pd.DataFrame(semua_data)

df = df.sort_values(by='Rating (1-5)', ascending=False).reset_index(drop=True)

output_file = 'scraping_book.csv'
df.to_csv(output_file, index=False, encoding='utf-8-sig')

print("=" * 55)
print(f"\n[DONE] Berhasil mengambil {len(df)} data buku dari {halaman - 1} halaman.")
print(f"[SAVE] Data tersimpan di: '{output_file}'")
print(f"\n[PREVIEW] 5 buku dengan rating tertinggi:")
print(df.head().to_string(index=False))
