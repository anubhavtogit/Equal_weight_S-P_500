import requests

# Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
API_KEY = 'E04GOGM84HG410ZX'
BASE_URL = 'https://www.alphavantage.co/query?'


def get_stock_data(stock_symbol):
    def get_stock_prices(symbol):
        endpoint = 'function=TIME_SERIES_DAILY'
        url = f'{BASE_URL}{endpoint}&symbol={symbol}&apikey={API_KEY}'

        try:
            response = requests.get(url)
            data = response.json()

            if 'Time Series (Daily)' in data:
                return data['Time Series (Daily)']
            else:
                print(f"Error: {data['Error Message']}")
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_market_cap(symbol):
        endpoint = 'function=GLOBAL_QUOTE'
        url = f'{BASE_URL}{endpoint}&symbol={symbol}&apikey={API_KEY}'

        try:
            response = requests.get(url)
            data = response.json()

            if 'Global Quote' in data:
                return data['Global Quote']['MarketCapitalization']
            else:
                print(f"Error: {data['Error Message']}")
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    stock_prices = get_stock_prices(stock_symbol)
    market_cap = get_market_cap(stock_symbol)

    if stock_prices and market_cap:
        print(f"Stock prices for {stock_symbol}:")
        for date, info in stock_prices.items():
            print(
                f"{date}: Open - {info['1. open']}, High - {info['2. high']}, Low - {info['3. low']}, Close - {info['4. close']}, Volume - {info['5. volume']}")

        print(f"\nMarket Capitalization for {stock_symbol}: {market_cap}")


# Example usage in a Jupyter Notebook cell:
# Provide the stock symbol when calling the function
#get_stock_data('AAPL')  # Replace 'AAPL' with the desired stock symbol
