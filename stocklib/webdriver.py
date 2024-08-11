import requests
from lxml import html


def scrape_url_by_requirement(fund_symbol, requirement):
    """Scrape a URL by requirement.

    :param fund_symbol: Fund symbol to scrape.
    :type fund_symbol: str
    :param requirement: Requirement to scrape {Performance, Summary, History... etc}
    :type requirement: str
    :return: URL to scrape.
    :rtype: str
    """
    base_url = "https://finance.yahoo.com/quote"
    url = f"{base_url}/{fund_symbol}?p={fund_symbol}&.tsrc=fin-srch"
    if requirement == "performance":
        url = f"{base_url}/{fund_symbol}/performance?p={fund_symbol}"
    return url


def scrape_by_path(fund_symbol, xpath, performance="summary"):
    """Scrape a website by path.

    :param fund_symbol: Fund symbol to scrape.
    :type fund_symbol: str
    :param xpath: XPath to scrape.
    :type xpath: str
    :param performance: This tells us what page we want to scrape from YFinance, defaults to "summary"
    :type performance: str, optional
    :return: Scraped data.
    :rtype: str
    """
    # Construct the URL based on the fund_symbol and performance requirement
    url = scrape_url_by_requirement(fund_symbol, performance)
    
    # Fetch the content using requests
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve page with status code {response.status_code}")
    
    # Parse the HTML content
    tree = html.fromstring(response.content)
    
    # Extract data using XPath
    result_elements = tree.xpath(xpath)
    
    # Extract text from the elements
    result = ''.join([element.text_content().strip() for element in result_elements])
    
    return result
