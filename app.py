"""CodeAlpha Web Scraping - Book Price Scraper

This script scrapes book data from https://books.toscrape.com
and saves cleaned data to `data/books.csv`.
"""
import time
import sys
from urllib.parse import urljoin

import requests
import pandas as pd
from bs4 import BeautifulSoup


BASE_URL = "https://books.toscrape.com/"


def get_soup(url):
    """Fetch a URL and return a BeautifulSoup object.

    Uses a short timeout and raises for HTTP errors so the caller
    can handle them gracefully.
    """
    try:
        # Send GET request to the URL
        response = requests.get(url, timeout=10)
        # Raise an HTTPError for bad responses (4xx or 5xx)
        response.raise_for_status()
    except requests.RequestException as e:
        # Re-raise exception with context so caller can catch it
        raise RuntimeError(f"Error fetching {url}: {e}")

    # Parse the response HTML using lxml parser for speed and robustness
    return BeautifulSoup(response.text, "lxml")


def parse_rating(element):
    """Convert rating class to a human-readable number/string.

    The site encodes rating with classes like "star-rating Three".
    """
    classes = element.get("class", [])
    # Look for the rating word among classes
    ratings = [c for c in classes if c != "star-rating"]
    return ratings[0] if ratings else None


def extract_book_data(product, page_url):
    """Extract book information from a product element on a listing page.

    Returns a dict with keys: title, price, rating, availability, product_url
    """
    # Title is stored in the <a> tag's title attribute inside <h3>
    title_tag = product.find("h3").find("a")
    title = title_tag.get("title", "").strip()

    # Price is inside a <p class="price_color"> element
    price_tag = product.find("p", class_="price_color")
    price = price_tag.text.strip() if price_tag else None

    # Rating is encoded in the class of <p class="star-rating ...">
    rating_tag = product.find("p", class_="star-rating")
    rating = parse_rating(rating_tag) if rating_tag else None

    # Availability is inside a <p class="instock availability"> element
    availability_tag = product.find("p", class_="instock availability")
    availability = availability_tag.text.strip() if availability_tag else None

    # Product URL (relative) is in the href of the <a> tag; make it absolute
    partial_url = title_tag.get("href", "")
    product_url = urljoin(page_url, partial_url)

    return {
        "title": title,
        "price": price,
        "rating": rating,
        "availability": availability,
        "product_url": product_url,
    }


def extract_category_from_product(product_url):
    """Visit the product page and extract the category from the breadcrumb.

    This requires an extra HTTP request per product but ensures category
    accuracy for this beginner-friendly example.
    """
    try:
        soup = get_soup(product_url)
    except RuntimeError:
        return None

    # Breadcrumb structure: Home > Books > Category > Book Title
    breadcrumb = soup.find("ul", class_="breadcrumb")
    if not breadcrumb:
        return None

    items = [li.get_text(strip=True) for li in breadcrumb.find_all("li")]
    # The category is typically the second-to-last item (before the title)
    if len(items) >= 3:
        return items[-2]
    return None


def scrape_books(start_url):
    """Scrape all books by following pagination links starting from start_url.

    Returns a list of dicts with book data.
    """
    books = []
    page_url = start_url
    page_count = 0

    print("====================================")
    print("CodeAlpha Web Scraping Project")
    print("====================================")
    print("Connecting to Website...")

    while page_url:
        page_count += 1
        try:
            soup = get_soup(page_url)
        except RuntimeError as e:
            print(f"Failed to fetch page: {e}")
            break

        # Find all product containers on the page
        product_list = soup.select("ol.row li")

        for product in product_list:
            data = extract_book_data(product, page_url)
            # Extract category by visiting the product page
            data["category"] = extract_category_from_product(data["product_url"]) or "Unknown"
            books.append(data)

        print(f"Page {page_count} Completed")

        # Find the 'next' page link; if none, we are done
        next_li = soup.find("li", class_="next")
        if next_li and next_li.find("a"):
            next_href = next_li.find("a").get("href")
            # Build absolute URL for the next page
            page_url = urljoin(page_url, next_href)
            # Be polite and sleep a short time
            time.sleep(1)
        else:
            page_url = None

    print("Data Scraping Completed")
    return books


def clean_and_save(books, output_path):
    """Clean raw data and save to CSV at output_path.

    Cleaning steps:
    - Normalize column names
    - Strip extra spaces
    - Handle missing values
    - Remove duplicates
    """
    # Convert list of dicts to DataFrame
    df = pd.DataFrame(books)

    # Standardize column names (lowercase, underscores)
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # Strip strings and replace empty strings with NaN
    for col in df.select_dtypes(include=[object]).columns:
        df[col] = df[col].astype(str).str.strip()
        df[col].replace({"": pd.NA, "None": pd.NA}, inplace=True)

    # Remove duplicate records based on product_url
    if "product_url" in df.columns:
        df.drop_duplicates(subset=["product_url"], inplace=True)

    # Save to CSV
    df.to_csv(output_path, index=False)
    return df


def main():
    """Main entry point for the scraper script."""
    try:
        print("Website Connected Successfully.")
        print("Scraping Books...")

        # Start scraping from the base site
        books = scrape_books(BASE_URL)

        # Clean data and save to CSV
        df = clean_and_save(books, "data/books.csv")

        print("Data Cleaning Completed")
        print("CSV Saved Successfully")
        print("Location:")
        print("data/books.csv")
        print(f"Total Books Scraped: {len(df)}")
        print("Project Completed Successfully.")

    except Exception as e:
        # Catch-all to ensure beginner-friendly error message
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
