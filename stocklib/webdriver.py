"""Module to operate with webdrivers and scraping."""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrape_url_by_requirement(fund_symbol, requirement):
    """Scrape a URL by requirement.

    :param fund_symbol: Fund symbol to scrape.
    :type fund_symbol: String
    :param requirement: Requirement to scrape {Performance, Summary, History... etc}
    :type requirement: String
    :return: URL to scrape.
    :rtype: String
    """
    url = f"https://finance.yahoo.com/quote/{fund_symbol}?p={fund_symbol}&.tsrc=fin-srch"
    if requirement == "performance":
        url = f"https://finance.yahoo.com/quote/{fund_symbol}/performance?p={fund_symbol}"
    return url


def scrape_by_path(fund_symbol, xpath, performance="summary"):
    """Scrape a website by path.

    :param fund_symbol: Fund symbol to scrape.
    :type fund_symbol: String
    :param xpath: Xpath to scrape.
    :type xpath: String
    :param performance: This tells us what page we want to scrape from YFinance , defaults to "summary"
    :type performance: String, optional
    :return: Scraped data.
    :rtype: String
    """
    # Configure Selenium options
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1980,1020")
    options.add_argument('--disable-gpu')

    # Set path to your chromedriver executable
    driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)

    # Start the WebDriver and load the Morningstar website
    # service = Service(chromedriver_path)
    # driver = webdriver.Chrome(service=service, options=options)

    # Load the URL to scrape
    url = scrape_url_by_requirement(fund_symbol, performance)
    driver.get(url)

    # Wait for the expense ratio element to be visible
    result_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )

    # Extract the expense ratio text
    result = result_element.text.strip()

    # Close the WebDriver
    driver.quit()

    return result
