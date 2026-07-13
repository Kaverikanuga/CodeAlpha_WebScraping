# CodeAlpha Web Scraping – Book Price Scraper

## Project Description

This beginner-friendly Python project scrapes book information from https://books.toscrape.com using `requests` and `BeautifulSoup`. The scraper collects book title, price, rating, availability, product URL, and category, then saves cleaned data to `data/books.csv` using `pandas`.

## Features
- Scrapes multiple pages using pagination
- Extracts title, price, rating, availability, product URL, and category
- Handles HTTP errors gracefully
- Cleans data and removes duplicates
- Saves results to CSV (`data/books.csv`)

## Technologies Used
- Python 3.8+
- requests
- beautifulsoup4
- pandas
- lxml

## Folder Structure

CodeAlpha_WebScraping/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
│── data/
│   └── books_sample.csv
│── output/
│   └── .gitkeep
│── screenshots/
    └── .gitkeep

## Purpose of Files
- `app.py`: Main scraper script. Connects to site, parses pages, extracts and cleans data, and writes CSV.
- `requirements.txt`: Lists Python dependencies.
- `README.md`: Project documentation and instructions.
- `.gitignore`: Files and folders to ignore in Git.
- `data/books_sample.csv`: Example of expected CSV output format.
- `data/books.csv`: (Generated) Final CSV produced by running the script.
- `output/`: Folder for any exported outputs or additional artifacts.
- `screenshots/`: Place to store screenshots for the README or demonstration.

## Installation Guide

1. Clone the repository or download the project folder.
2. Create a virtual environment and activate it (see commands below).
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## How to Run

1. Ensure your virtual environment is active and dependencies are installed.
2. Run the scraper:

```bash
python app.py
```

Expected output: The script will print progress messages and save `data/books.csv`.

## Expected Output (Sample)

Sample terminal output is shown in the project documentation and a small sample CSV is provided at `data/books_sample.csv`.

## Screenshots

Place screenshots of the running script and sample CSV in the `screenshots/` folder and reference them here.

## Future Improvements
- Add command-line options (e.g., limit pages, output path)
- Parallelize product page fetches for speed
- Add more robust retry/backoff strategy for network errors
- Export to JSON or a database

## Author

CodeAlpha Intern - Your Name Here

## Running in VS Code (Quick Steps)

1. Open the folder in VS Code: `File -> Open Folder...` and select the project folder.
2. Open a new terminal in VS Code.
3. Create and activate a virtual environment (commands below).
4. Install dependencies and run `python app.py`.

## Virtual Environment Commands (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Git / GitHub Commands

```bash
git init
git add .
git commit -m "Initial commit - CodeAlpha Web Scraping Project"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

## Recording a Demo Video
1. Prepare a short script (see sample below).
2. Record your screen while running the scraper.
3. Show the terminal output and open `data/books.csv` in a spreadsheet viewer.
4. Save the recording and upload to your portfolio or submit as requested.

## LinkedIn Post (Professional)

I recently completed a beginner-friendly web scraping project for the CodeAlpha Data Analytics Internship. Using Python, Requests, BeautifulSoup, and Pandas, I built a scraper that collected book titles, prices, ratings, availability, product URLs, and categories from books.toscrape.com, cleaned the data, and saved it to CSV. This project helped me practice HTML parsing, pagination handling, and data cleaning. Check out the repo and sample output! #DataAnalytics #WebScraping #Python

## 2–3 Minute Project Explanation Script

Hi, I'm [Your Name]. For my CodeAlpha internship task, I built a Python web scraper that collects book information from books.toscrape.com. The scraper navigates through all pages, extracts title, price, rating, availability, product URL, and category, and saves cleaned results to a CSV file. I used `requests` to fetch pages, `BeautifulSoup` to parse HTML, and `pandas` to clean and save the dataset. Key learning outcomes included handling pagination, parsing nested HTML structures, and ensuring robust error handling for network requests. The repository includes instructions to run the project locally and sample output for reference.
