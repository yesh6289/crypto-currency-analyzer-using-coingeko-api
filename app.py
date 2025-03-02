# Import required libraries
import pandas as pd
import requests
import time

# Function to fetch live cryptocurrency data
def get_crypto_data():
    """Fetches the top 50 cryptocurrencies data from CoinGecko API."""
    endpoint = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
        "sparkline": False,
    }

    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None  # Return None if API call fails

# Function to process the data
def process_data(data):
    """Processes the raw data into a DataFrame and extracts key statistics."""
    if not data:
        return None, None, None, None, None

    # Create DataFrame with required columns
    data_frame = pd.DataFrame(data, columns=['name', 'symbol', 'current_price', 'market_cap', 'total_volume', 'price_change_percentage_24h'])

    # Extract key metrics
    top_performer = data_frame.nlargest(5, 'market_cap')
    average_price = data_frame['current_price'].mean()
    max_price_change = data_frame['price_change_percentage_24h'].max()
    min_price_change = data_frame['price_change_percentage_24h'].min()

    return data_frame, top_performer, average_price, max_price_change, min_price_change

# Function to update the Excel file
def update_xls(data_frame):
    """Writes the DataFrame to an Excel spreadsheet."""
    if data_frame is None:
        print("No data to export.")
        return

    with pd.ExcelWriter('crypto_live.xlsx', engine='xlsxwriter') as writer:
        data_frame.to_excel(writer, sheet_name='MarketSnapshot', index=False)

    print("Data successfully written to Excel file.")

# Main function to run the script continuously
def main():
    """Fetches and updates cryptocurrency data every 5 minutes."""
    while True:
        print("\nFetching live cryptocurrency data...")
        data = get_crypto_data()

        if data is not None:
            processed_data = process_data(data)
            if processed_data:
                data_frame, top_performer, average_price, max_price_change, min_price_change = processed_data

                # Print key statistics
                print("\nTop 5 Cryptocurrencies by Market Capitalization:\n", top_performer)
                print(f"\nAverage Cryptocurrency Price: ${average_price:.2f}")
                print(f"Maximum 24-Hour Price Increase: {max_price_change:.2f}%")
                print(f"Minimum 24-Hour Price Decrease: {min_price_change:.2f}%")

                # Save data to Excel
                update_xls(data_frame)
            else:
                print("Data processing failed.")
        else:
            print("Skipping update due to API failure.")

        print("\nWaiting for 5 minutes before next update...")
        time.sleep(300)  # Wait 5 minutes before fetching data again

# Run the script
if __name__ == "__main__":
    main()
