# Stock Data Puller

This project was to help me figure out what I want to do with my investment portfolio.

Currently I'm holding more than 100 stocks and I want to figure out if I need to re-balance or make any changes.

We use mainly YFinance and we are looking to add more data we can scrape from to make better decisions.

Decisions so far are based on the following:
- [x] Beta Indicator & Recommendation
- [x] EBITDA Margins & Recommendation
- [x] D/E Ratio & Recommendation
- [x] P/E Ratio & Recommendation

We are currently working on improving the recommendations and adding more data to the mix.

Feel free to create a ticket and we'll make sure to continue improving it.

Coming soon:
- [ ] Industry
- [ ] API Access to get data

## Installation

## Docker

```bash
docker build -t stock-data-puller .
docker run -it stock-data-puller
```

## Python

```bash
# Create a virtualenv:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python process_csv_data.py --help
python process_csv_data.py -i stock_data.csv -o stock_data_processed.csv
```
