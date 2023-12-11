import pandas as pd
import yfinance as yf

def calculate_covariance(stock_data):
    """
    Calculate the covariance matrix of stock returns.

    Parameters:
    - stock_data (pandas DataFrame): DataFrame of stock prices with dates as index and tickers as columns.

    Returns:
    - pandas DataFrame: Covariance matrix of the stock returns.
    """
    # Calculate daily returns
    returns = stock_data.pct_change().dropna()

    # Calculate the covariance matrix
    covariance_matrix = returns.cov()

    return covariance_matrix

