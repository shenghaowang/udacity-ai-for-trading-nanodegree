import pandas as pd
import numpy as np
import operator

def get_most_volatile(prices):
    """Return the ticker symbol for the most volatile stock.

    Parameters
    ----------
    prices : pandas.DataFrame
        a pandas.DataFrame object with columns: ['ticker', 'date', 'price']

    Returns
    -------
    ticker : string
        ticker symbol for the most volatile stock
    """
    tickers = prices['ticker'].unique()
    volatility = {}
    for ticker in tickers:
        volatility[ticker] = prices['price'].loc[prices['ticker'] == ticker].std()

    return max(volatility.items(), key=operator.itemgetter(1))[0]


def test_run(filename='prices.csv'):
    """Test run get_most_volatile() with stock prices from a file."""
    prices = pd.read_csv(filename, parse_dates=['date'])
    print("Most volatile stock: {}".format(get_most_volatile(prices)))


if __name__ == '__main__':
    test_run()

