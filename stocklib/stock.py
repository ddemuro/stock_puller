"""This module contains functions to get stock information from Yahoo Finance."""
import yfinance as yf
import datetime
from stocklib.general import debug_print, convert_epoch_to_date
from stocklib.numbers import convert_number_to_string_text
from stocklib.webdriver import scrape_by_path


def get_stock_info(symbol):
    """Get all data for a symbol of our interest

    :param symbol: Stock symbol to get data for
    :type symbol: String
    :return: All data for a symbol of our interest
    :rtype: Dictionary
    """
    stock = yf.Ticker(symbol)
    # history = stock.history(period='1d')
    # Get the current date
    # current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Define the start and end dates for each time period
    # last_close_ago = (datetime.datetime.now() - datetime.timedelta(days=5)).strftime("%Y-%m-%d")
    # one_year_ago = (datetime.datetime.now() - datetime.timedelta(days=365)).strftime("%Y-%m-%d")
    # five_years_ago = (datetime.datetime.now() - datetime.timedelta(days=5 * 365)).strftime("%Y-%m-%d")
    # ten_years_ago = (datetime.datetime.now() - datetime.timedelta(days=10 * 365)).strftime("%Y-%m-%d")
    # eleven_years_ago = (datetime.datetime.now() - datetime.timedelta(days=11 * 365)).strftime("%Y-%m-%d")

    # Retrieve the data using yfinance
    # data = yf.download(symbol, start=ten_years_ago, end=current_date)

    # Extract the last close prices for each time period
    # last_close = data.loc[last_close_ago:current_date]['Close'].iloc[-1]
    # last_close_1_year = data.loc[datetime.datetime(datetime.datetime.now().year-1, 1, 1):datetime.datetime(datetime.datetime.now().year-1, 12, 31)]['Close'].iloc[-1]
    # last_close_5_years = data.loc[datetime.datetime(datetime.datetime.now().year-5, 1, 1):datetime.datetime(datetime.datetime.now().year-5, 12, 31)]['Close'].iloc[-1]
    # last_close_10_years = data.loc[datetime.datetime(datetime.datetime.now().year-9, 1, 1):datetime.datetime(datetime.datetime.now().year-9, 12, 31)]['Close'].iloc[-1]

    # Calculate year-to-date performance
    end_date = datetime.datetime.today().strftime('%Y-%m-%d')
    start_date = datetime.datetime(
        datetime.datetime.today().year, 1, 1).strftime('%Y-%m-%d')
    data = yf.download(symbol, start=start_date, end=end_date)
    closing_prices = data['Close']
    price_calculated = (closing_prices[-1] - closing_prices[0]) / closing_prices[0] * 100
    ytd_performance = round(price_calculated, 3)
    debug_print(ytd_performance)

    # Calculate 1-year performance
    start_date = datetime.datetime(
        datetime.datetime.today().year-1, 1, 1).strftime('%Y-%m-%d')
    end_date = datetime.datetime(
        datetime.datetime.today().year-1, 12, 31).strftime('%Y-%m-%d')
    data = yf.download(symbol, start=start_date, end=end_date)
    closing_prices = data['Close']
    price_calculated = (closing_prices[-1] - closing_prices[0]) / closing_prices[0] * 100
    one_year_performance = round(price_calculated, 3)
    debug_print(one_year_performance)

    # Calculate 5-year performance
    start_date = datetime.datetime(
        datetime.datetime.today().year-5, 1, 1).strftime('%Y-%m-%d')
    end_date = datetime.datetime(
        datetime.datetime.today().year-1, 12, 31).strftime('%Y-%m-%d')
    data = yf.download(symbol, start=start_date, end=end_date)
    closing_prices = data['Close']
    price_calculated = (closing_prices[-1] - closing_prices[0]) / closing_prices[0] * 100
    five_year_performance = round(price_calculated, 3)
    debug_print(five_year_performance)

    # Calculate 10-year performance
    start_date = datetime.datetime(
        datetime.datetime.today().year-10, 1, 1).strftime('%Y-%m-%d')
    end_date = datetime.datetime(
        datetime.datetime.today().year-1, 12, 31).strftime('%Y-%m-%d')
    data = yf.download(symbol, start=start_date, end=end_date)
    closing_prices = data['Close']
    price_calculated = (closing_prices[-1] - closing_prices[0]) / closing_prices[0] * 100
    ten_year_performance = round(price_calculated, 3)
    debug_print(ten_year_performance)

    # Get dividend information
    dividend = 'N/A'
    if 'trailingAnnualDividendRate' in stock.info:
        dividend = stock.info['trailingAnnualDividendRate']
    debug_print(dividend)

    market_cap = 'N/A'
    if 'marketCap' in stock.info:
        market_cap = convert_number_to_string_text(stock.info['marketCap'])

    # Get expense ratio
    expense_ratio = 'N/A'
    eratio = scrape_by_path(symbol, "//*[@id='quote-summary']/div[2]/table/tbody/tr[7]/td[2]")
    if "%" in eratio:
        expense_ratio = eratio
    debug_print(expense_ratio)

    last_split_date = 'N/A'
    if 'lastSplitDate' in stock.info:
        last_split_date = convert_epoch_to_date(stock.info['lastSplitDate'])

    # Get P/E ratio
    pe_ratio = 'N/A'
    rpe_ratio = 'N/A'
    if 'trailingPE' in stock.info:
        pe_ratio = round(stock.info['trailingPE'], 3)
        rpe_ratio = 'FAIR PE'
        if pe_ratio > 24:
            rpe_ratio = 'OVERVALUED'
        if pe_ratio > 15 and pe_ratio < 24:
            rpe_ratio = 'FAIR VALUE'
        if pe_ratio < 15:
            rpe_ratio = 'UNDERVALUED'
        if pe_ratio < 0:
            rpe_ratio = 'NEGATIVE P/E'
    debug_print(pe_ratio)

    # Last Split Factor
    last_split_factor = 'N/A'
    if 'lastSplitFactor' in stock.info:
        last_split_factor = stock.info['lastSplitFactor']
    debug_print(last_split_factor)

    recommendation = 'N/A'
    if 'recommendationKey' in stock.info:
        recommendation = stock.info['recommendationKey']
    debug_print(recommendation)

    beta_indicator = 'N/A'
    if 'beta' in stock.info:
        beta_indicator = stock.info['beta']

    rbeta_indicator = 'N/A'
    if beta_indicator != 'N/A':
        rbeta_indicator = 'BETA OK'
        if beta_indicator > 1.5:
            rbeta_indicator = 'EXTREME RISK (Riskier than S&P 500)'
        if beta_indicator > 1.2 and beta_indicator < 1.5:
            rbeta_indicator = 'HIGH RISK (Riskier than S&P 500)'
        if beta_indicator > 1 and beta_indicator < 1.2:
            rbeta_indicator = 'OK (Same as S&P 500))'
        if beta_indicator < 1:
            rbeta_indicator = 'LOW RISK (Safer than S&P 500)'

    five_year_div_yld = 'N/A'
    if 'fiveYearAvgDividendYield' in stock.info:
        five_year_div_yld = round(stock.info['fiveYearAvgDividendYield'], 3)
    debug_print(five_year_div_yld)

    debt_to_equity = 'N/A'
    rdebt_to_equity = 'N/A'
    if 'debtToEquity' in stock.info:
        debt_to_equity = round(stock.info['debtToEquity'], 3)
        rdebt_to_equity = 'D/E OK'
        if debt_to_equity < 0 and debt_to_equity > 2.5:
            rdebt_to_equity = 'WARNING D/E'
    debug_print(debt_to_equity)

    ebitda_margins = 'N/A'
    rebitda_margins = 'N/A'
    if 'ebitdaMargins' in stock.info:
        ebitda_margins = stock.info['ebitdaMargins']
        rebitda_margins = 'EBITDA MARGINS OK'
        if ebitda_margins < 10:
            rebitda_margins = 'LOW EBITDA MARGINS'
    debug_print(ebitda_margins)

    return {
        'Symbol': symbol,
        'Market Cap': market_cap,
        'YTD': ytd_performance,
        '1-Year': round(one_year_performance, 3),
        '5-Year': round(five_year_performance, 3),
        '10-Year': round(ten_year_performance, 3),
        'Dividend': dividend,
        'Last Split Factor': last_split_factor,
        'Last Split Date': last_split_date,
        'Expense Ratio': expense_ratio,
        'Recommend Operation': recommendation,
        'Beta Indicator': beta_indicator,
        'Recommend. Beta Indicator': rbeta_indicator,
        '5-Year Div. Yield': five_year_div_yld,
        'Debt to Equity': debt_to_equity,
        'EBITDA Margins': ebitda_margins,
        'Recommend. EBITDA Margins': rebitda_margins,
        'Recommend. D/E': rdebt_to_equity,
        'Recommend. P/E': rpe_ratio,
        'P/E': pe_ratio
    }
