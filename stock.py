import requests
import pandas as pd

# Alpha Vantage API configuration
API_KEY = 'NWC4AT60L84IKXAQ'
BASE_URL = 'https://www.alphavantage.co/query'

# Portfolio class
class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, shares):
        if symbol in self.stocks:
            self.stocks[symbol] += shares
        else:
            self.stocks[symbol] = shares

    def remove_stock(self, symbol, shares):
        if symbol in self.stocks:
            self.stocks[symbol] -= shares
            if self.stocks[symbol] <= 0:
                del self.stocks[symbol]
        else:
            print(f"Stock {symbol} not in portfolio.")

    def get_stock_data(self, symbol):
        params = {
            'function': 'TIME_SERIES_INTRADAY',
            'symbol': symbol,
            'interval': '5min',
            'apikey': API_KEY
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        if 'Time Series (5min)' in data:
            return data['Time Series (5min)']
        else:
            print(f"Error fetching data for {symbol}: {data}")
            return None

    def get_portfolio_value(self):
        total_value = 0.0
        for symbol, shares in self.stocks.items():
            data = self.get_stock_data(symbol)
            if data:
                latest_time = sorted(data.keys())[-1]
                latest_price = float(data[latest_time]['4. close'])
                total_value += latest_price * shares
        return total_value

    def display_portfolio(self):
        portfolio_df = pd.DataFrame(columns=['Symbol', 'Shares', 'Latest Price', 'Total Value'])
        for symbol, shares in self.stocks.items():
            data = self.get_stock_data(symbol)
            if data:
                latest_time = sorted(data.keys())[-1]
                latest_price = float(data[latest_time]['4. close'])
                total_value = latest_price * shares
                portfolio_df = portfolio_df.append({
                    'Symbol': symbol,
                    'Shares': shares,
                    'Latest Price': latest_price,
                    'Total Value': total_value
                }, ignore_index=True)
        print(portfolio_df)
        print(f"Total Portfolio Value: ${self.get_portfolio_value():.2f}")

# Example usage
if __name__ == '__main__':
    portfolio = Portfolio()
    portfolio.add_stock('AAPL', 10)
    portfolio.add_stock('MSFT', 5)
    portfolio.display_portfolio()
    portfolio.remove_stock('AAPL', 5)
    portfolio.display_portfolio()
