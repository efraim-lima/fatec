from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from Configuration import config


def fetch_page(url):
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    driver = config.webDriver()
    driver.get(url)
    html_content = driver.page_source
    driver.quit()
    return html_content

def extract_headings(html_content):
    headings = {'h1': [], 'h2': [], 'h3': []}
    soup = BeautifulSoup(html_content, 'html.parser')
    for tag in ['h1', 'h2', 'h3']:
        headings[tag] = [heading.text.strip() for heading in soup.find_all(tag)]
    return headings

def main():
    url = 'https://example.com'  # Change this URL to the desired page
    html_content = fetch_page(url)
    if html_content:
        headings = extract_headings(html_content)
        print("H1 Headings:", headings['h1'])
        print("H2 Headings:", headings['h2'])
        print("H3 Headings:", headings['h3'])

if __name__ == "__main__":
    main()

