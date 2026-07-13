# 📚 CodeAlpha Web Scraping

A beginner-friendly Python Web Scraping project developed using **Python**, **Requests**, **BeautifulSoup**, and **Pandas**.

This project extracts book information from **BooksToScrape**, cleans the collected data, and exports it into a CSV file for further analysis.

---

# 📖 Table of Contents

- Project Overview
- Features
- Technology Stack
- Project Architecture
- Folder Structure
- Installation Guide
- Running the Project
- Output
- Screenshots
- Future Improvements
- Author

---

# 📌 Project Overview

The goal of this project is to demonstrate web scraping using Python.

The scraper automatically visits multiple pages, extracts book information, cleans the dataset, removes duplicates, and saves everything into a CSV file.

---

# ✨ Features

- Scrapes multiple pages
- Extracts book title
- Extracts price
- Extracts rating
- Extracts availability
- Extracts category
- Extracts product URL
- Cleans scraped data
- Removes duplicate records
- Saves data into CSV
- Beginner-friendly project

---

# 🛠 Technology Stack

## Programming Language

- Python 3

## Libraries

- Requests
- BeautifulSoup4
- Pandas
- lxml

## Version Control

- Git
- GitHub

---

# 🏗 Project Architecture

```
Website
   │
   ▼
Requests
   │
   ▼
BeautifulSoup
   │
   ▼
Extract Data
   │
   ▼
Clean Data
   │
   ▼
Pandas DataFrame
   │
   ▼
books.csv
```

---

# 📁 Folder Structure

```text
CodeAlpha_WebScraping/
│
├── data/
│   ├── books.csv
│   └── books_sample.csv
│
├── output/
│
├── screenshots/
│   ├── terminal_output.png
│   ├── books_csv.png
│   └── github_repo.png
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙ Installation Guide

## Clone Repository

```bash
git clone https://github.com/Kaverikanuga/CodeAlpha_WebScraping.git
```

Go inside project

```bash
cd CodeAlpha_WebScraping
```

Install libraries

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

```bash
python app.py
```

Expected Output

```
Data Cleaning Completed

CSV Saved Successfully

Location:
data/books.csv

Total Books Scraped: 1000

Project Completed Successfully.
```

---

# 📊 Output

The scraper generates

- Clean dataset
- CSV file
- 1000 book records

Saved inside

```
data/books.csv
```

---

# 📷 Screenshots

## Terminal Output

![Terminal Output](screenshots/terminal_output.png)

---

## CSV Output

![CSV Output](screenshots/books_csv.png)

---

## GitHub Repository

![GitHub](screenshots/github_repo.png)

---

# 🚀 Future Improvements

- Export to Excel
- Export to JSON
- Database Integration
- GUI Interface
- Scheduler Support
- Cloud Deployment

---

# 👩‍💻 Author

**Kaveri Kanuga**

CodeAlpha Internship Task 1

Python Web Scraping Project

GitHub:
https://github.com/Kaverikanuga
