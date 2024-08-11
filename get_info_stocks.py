""" This main program parses a csv provided by parameter and appends stock information to it in a new file."""

import argparse
import os
import csv
from stocklib.stock import get_stock_info


def main(file_name_in, filename_out="results.csv"):
    # Check if the file exists
    if not os.path.exists(file_name_in):
        print(f"Error: File '{file_name_in}' does not exist.")
        return

    # Open the file and process it
    with open(file_name_in, 'r') as csvfile:
        # Format is one ticker per line
        with open(filename_out, 'a', newline='') as csvfile_out:
            # Append the stock info to the output file
            fieldnames = ['Symbol', "Name in M1", "Shares", 'Market Cap', 'YTD', '1-Year', '5-Year',
                        '10-Year', 'Dividend', 'Expense Ratio', 'P/E', "Cost Basis",
                        "Unrealized Gain/Loss", "Unrealized Gain/Loss %", "Avg Price", "Cost Basis", 'Last Split Factor',
                        'Recommend Operation', '5-Year Div. Yield', 'Debt to Equity', 'EBITDA Margins',
                        'Recommend. EBITDA Margins', 'Recommend. D/E', 'Recommend. P/E', 'Last Split Date',
                        'Beta Indicator', 'Recommend. Beta Indicator', 'Date']
            writer = csv.DictWriter(csvfile_out, fieldnames=fieldnames)
            writer.writeheader()
            for row in csvfile:
                try:
                    stock_symbol = row.strip()
                    print("Getting stock information for " + stock_symbol)
                    stock_info = get_stock_info(stock_symbol)
                    print(stock_info)
                    writer.writerow(stock_info)
                except Exception as e:
                    print(f"Error processing {stock_symbol}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Console app to process tickers get extra data and recommendations.")
    parser.add_argument("-i", help="Path to the file to be checked one ticker per line.")

    args = parser.parse_args()

    main(args.i)
