# 🕷️ CodeAlpha Internship — Task 1: Web Scraping

This project is part of the **CodeAlpha Internship** program (Web Scraping Task).
This Python script scrapes book data from **[books.toscrape.com](http://books.toscrape.com/)** — a sandbox website designed for practicing web scraping techniques.

---

## 📋 Features

* ✅ Scrapes **all 50 pages** (~1,000 books) automatically
* ✅ Extracts: **Title**, **Price**, **Rating**, and **Stock Availability**
* ✅ Performs data cleaning (converts prices to float, maps star ratings to numerical values 1–5)
* ✅ Implements robust error handling for request failures
* ✅ Exports final structured dataset to **CSV** format
* ✅ Sorts data by **highest rating** by default

---

## 🛠️ Tech Stack & Dependencies

| Library | Purpose |
| --- | --- |
| `requests` | Handles HTTP GET requests to fetch web pages |
| `BeautifulSoup` | Parses and extracts data from HTML document structures |
| `pandas` | Manages data structures, cleans data, and exports to CSV |
| `time` | Introduces delays between requests to ensure ethical scraping |

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/lonelybunny69/CodeAlpha_webScraping.git
cd CodeAlpha_webScraping

```

### 2. Install dependencies

```bash
pip install requests beautifulsoup4 pandas

```

### 3. Run the script

```bash
python Task1.py

```

---

## 📁 Output Structure

Upon completion, the script generates `scraping_book.csv` in the root directory with the following schema:

| Column | Description | Data Type |
| --- | --- | --- |
| `Title` | Full title of the book | String |
| `Price (£)` | Book price in British Pounds | Float |
| `Rating (1-5)` | Numerical rating from 1 to 5 | Integer |
| `Stock` | Availability status | String |

---

## 📊 Sample Output

```
Title                                            Price (£)  Rating (1-5)  Stock
It's Only the Himalayas                            45.17             5  In stock
Full Moon over Noah's Ark                          49.43             5  In stock
...

```

---

## 👤 Author

**Name:** M. Syakira Hamidan

**Program:** CodeAlpha Internship — Web Scraping Task

**Target Site:** [books.toscrape.com](http://books.toscrape.com/)