"""
Exercise: Web Scraping

Project: Web Scraping with requests and BeautifulSoup (Selenium-enhanced)

Goal:
Use web scraping techniques to extract information from a webpage.

You should extract:
- The title of the webpage
- Product/book titles from a specific HTML class
- Image links associated with the products

Input:
- A URL to scrape
- An HTML class name for locating product data

Output:
- Page title
- A list of product titles
- A list of image URLs

Notes:
- Use Selenium to handle pages that require JavaScript scrolling.
- Use BeautifulSoup to parse and extract HTML content.
"""

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_dynamic_page_source(url: str, scrolls: int = 5, scroll_pause: int = 2) -> str:
    """
    Load a dynamic web page using Selenium and return the final HTML after scrolling.
    """
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    time.sleep(scroll_pause)

    for _ in range(scrolls):
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(scroll_pause)
        if driver.execute_script('return window.innerHeight + window.pageYOffset') >= \
           driver.execute_script('return document.body.scrollHeight'):
            break

    page_source = driver.page_source
    driver.quit()
    return page_source


def extract_book_data(html: str, limit: int = 15) -> None:
    """
    Extract and print the site title, book titles, and image URLs from the given HTML.
    """
    soup = BeautifulSoup(html, 'html.parser')

    # Page title
    title_tag = soup.find('title')
    print(
        f"\nSite Title:\n{title_tag.text.strip() if title_tag else 'No title found'}\n")

    # Book cards
    books = soup.find_all(class_="bookCard_book__6dU_a")

    for book in books[:limit]:
        book_title = book.find(class_="bookCard_bookTitle__ELp4O")
        img_tag = book.find("img", class_="bookCard_bookCover__1L_jX")

        if book_title:
            print(f"Title: {book_title.text.strip()}")
        else:
            print("Title: [Not found]")

        if img_tag and img_tag.get("src"):
            print(f"Image: {img_tag['src']}")
        else:
            print("Image: [Not found]")

        print()


def main():
    """
    Main function to run the web scraping project.
    """
    url = "https://taaghche.com/filter?filter-bookType=1&filter-price=-200000&filter-target=1&order=1"
    html = get_dynamic_page_source(url)
    extract_book_data(html)


if __name__ == "__main__":
    main()
