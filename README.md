# crypto-currency-analyzer-using-coingeko-api
# Live Cryptocurrency Data Analysis

## Overview
This Python script fetches live cryptocurrency data for the **top 50** cryptocurrencies by market capitalization using the **CoinGecko API**. It updates an Excel file every **5 minutes** with the latest prices and key metrics.

## Features
- Fetches **live cryptocurrency data** from CoinGecko.
- Extracts key statistics:
  - **Top 5 cryptocurrencies** by market capitalization.
  - **Average price** of the top 50 cryptocurrencies.
  - **Highest and lowest** 24-hour percentage price change.
- Saves the data to an **Excel file (`crypto_live.xlsx`)** that updates every **5 minutes**.

## Requirements
Before running the script, ensure you have the following Python packages installed:

```bash
pip install pandas requests xlsxwriter
```
How to Run the Script
Clone this repository or download the script file.
Open a terminal and navigate to the script's directory.
Run the script using:
```bash
python app.py
```

The script will fetch live data, display key statistics, and update crypto_live.xlsx every 5 minutes.
Output
The script prints the top-performing cryptocurrencies and key statistics in the console.
An Excel file (crypto_live.xlsx) is updated with the latest data.
Example Output
```yaml
Fetching live cryptocurrency data...

Top 5 Cryptocurrencies by Market Capitalization:
      name    symbol  current_price    market_cap  ...
0  Bitcoin      BTC       50000.00  1.2 Trillion  ...
1  Ethereum     ETH        3500.00  420 Billion  ...
...

Average Cryptocurrency Price: $5123.45
Maximum 24-Hour Price Increase: 8.5%
Minimum 24-Hour Price Decrease: -3.2%

Data successfully written to Excel file.
Waiting for 5 minutes before next update...
```
Notes
Ensure you have a stable internet connection for continuous updates.
The script runs indefinitely—use Ctrl+C to stop execution.
API rate limits may apply; if the API call fails, the script will retry in 5 minutes.
Contact
For any queries, reach out at nagulayeshwanth2004@gmail.com \.

