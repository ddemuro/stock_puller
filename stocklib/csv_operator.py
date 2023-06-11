""" This file contains functions to read and write CSV files. """
import csv
from stocklib.stock import get_stock_info
from stocklib.general import debug_print
from specific_broker.m1_process import sanitize_m1


def append_stock_info_to_csv(stock_info, filename, write_header=False):
    """Stock information to CSV file to save.

    :param stock_info: Information to save.
    :type stock_info: Dictionary
    :param filename: Filename to save to.
    :type filename: String
    :param write_header: Define if we need to write header, defaults to False
    :type write_header: bool, optional
    """
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['Symbol', "Name in M1", "Shares", 'Market Cap', 'YTD', '1-Year', '5-Year',
                      '10-Year', 'Dividend', 'Expense Ratio', 'P/E', "Cost Basis",
                      "Unrealized Gain/Loss", "Unrealized Gain/Loss %", "Avg Price", "Cost Basis", 'Last Split Factor',
                      'Recommend Operation', '5-Year Div. Yield', 'Debt to Equity', 'EBITDA Margins',
                      'Recommend. EBITDA Margins', 'Recommend. D/E', 'Recommend. P/E', 'Last Split Date',
                      'Beta Indicator', 'Recommend. Beta Indicator']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
        writer.writerow(stock_info)


# Read stock symbols from CSV file
def read_stock_symbols_from_csv(filename_in, filename_out):
    """Read stock symbols from CSV file.

    :param filename: CSV filename to read.
    :type filename: String
    """
    with open(filename_in, 'r') as csvfile:
        reader = csv.reader(csvfile)
        write_header = True
        next(reader)  # Skip header row
        for row in reader:
            stock_symbol = row[0].strip()
            print("Getting stock information for " + stock_symbol)
            stock_info = get_stock_info(stock_symbol)
            stock_info.update(sanitize_m1(row))
            append_stock_info_to_csv(stock_info, filename_out, write_header)
            debug_print("Turning off first row since we're moving to next")
            write_header = False
