""" This main program parses a csv provided by parameter and appends stock information to it in a new file."""

import argparse
import os
from stocklib.csv_operator import read_stock_symbols_from_csv


def main(file_name_in, filename_out):
    # Check if the file exists
    if not os.path.exists(file_name_in):
        print(f"Error: File '{file_name_in}' does not exist.")
        return

    if os.path.isfile(filename_out):
        print(f"Error: File '{filename_out}' exists.")
        return

    # Add your code here to perform operations on the file
    read_stock_symbols_from_csv(file_name_in, filename_out)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Console app to process M1 Holding and get extra data and recommendations.")
    parser.add_argument("-i", help="Path to the file to be checked and processed (M1 export).")
    parser.add_argument("-o", help="File name to write the modified data to.")

    args = parser.parse_args()

    main(args.i, args.o)
