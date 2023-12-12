import click
import yfinance as yf
from .covariance import calculate_covariance, calculate_portfolio_balance, optimize_weights
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@click.group()
def cli():
    pass

@cli.command(help='<start date> <end date> <tickers>. Graph stock data for given tickers and date range.')
@click.argument('start_date')
@click.argument('end_date')
@click.argument('ticker_symbols', nargs=-1)
def view(start_date, end_date, ticker_symbols):
    plt.figure(figsize=(10, 6))

    for ticker_symbol in ticker_symbols:
        ticker_data = yf.Ticker(ticker_symbol)
        historical_data = ticker_data.history(start=start_date, end=end_date)

        plt.plot(historical_data['Close'], label=f'{ticker_symbol} Close Price')

    plt.title(f'Stock Prices ({start_date} to {end_date})')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()

@cli.command(help='<start date> <end date> <tickers>. Find the covariance matrix for a set of stocks. Use --file <file path> to save data to a file.')
@click.option('--file', 'file_path', type=str, help='Path to save the CSV file containing the covariance matrix')
@click.argument('start_date', required=True, type=str)
@click.argument('end_date', required=True, type=str)
@click.argument('tickers', required=True, nargs=-1)
def covariance(file_path, start_date, end_date, tickers):
    try:
        stock_data = yf.download(list(tickers), start=start_date, end=end_date)['Adj Close']
        
        covariance_matrix = calculate_covariance(stock_data)

        # Print or save the covariance matrix
        if file_path:
            covariance_matrix.to_csv(file_path)
            click.echo(f'Covariance matrix saved to: {file_path}')
        else:
            click.echo(covariance_matrix.to_string())

    except Exception as e:
        click.echo(f'Error: {e}')

@cli.command(help = '<directory> <start date> <end date> <ticker symbols>. Download the requested tickers historical price data for a range of time')
@click.argument('directory')
@click.argument('start_date')
@click.argument('end_date')
@click.argument('tickers', nargs=-1)
def download(directory, start_date, end_date, tickers):
    ticker_list = list(tickers)

    data = yf.download(ticker_list, start=start_date, end=end_date)

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = [' '.join(col).strip() for col in data.columns.values]

    data.reset_index(inplace=True)
    data['Date'] = data['Date'].dt.strftime('%Y-%m-%d')

    filename = os.path.join(directory, 'stock_data.csv')

    data.to_csv(filename, index=False)

    click.echo(f'Stock data saved to {filename}')

@cli.command(help='<covariance_matrix_filepath>. Calculate the minimum variance portfolio weights.')
@click.argument('covariance_matrix_filepath')
def weight(covariance_matrix_filepath):
    try:
        covariance_dataframe = pd.read_csv(covariance_matrix_filepath, index_col=0)
        matrix = covariance_dataframe.to_numpy()

        weights = optimize_weights(matrix)

        stock_names = covariance_dataframe.columns
        weights_dict = dict(zip(stock_names, weights))

        click.echo("Minimum Variance Portfolio Weights:")
        for stock, weight in weights_dict.items():
            click.echo(f"{stock}: {weight:.4f}")

    except Exception as e:
        click.echo(f"Error: {e}")


@cli.command(help='<start date> <end date> <ticker> <weight>. Calculate the return of a portfolio for a given time frame, tickers, and weights.')
@click.argument('start_date')
@click.argument('end_date')
@click.argument('tickers_and_weights', nargs=-1)
def returns(start_date, end_date, tickers_and_weights):
    try:
        if len(tickers_and_weights) % 2 != 0:
            raise ValueError("Please provide an even number of arguments (ticker and weight pairs).")

        tickers = tickers_and_weights[::2]
        weights = np.array(tickers_and_weights[1::2], dtype=float)

        if np.sum(weights) != 1:
            raise ValueError("Sum of weights must be equal to 1.")
        

        data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']

        daily_returns = data.pct_change().dropna()

        portfolio_returns = daily_returns.dot(weights)

        total_return = (1 + portfolio_returns).prod() - 1
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(daily_returns.cov(), weights)))

        click.echo(f"Total Portfolio Return: {total_return * 100:.2f}%")
        click.echo(f"Portfolio Volatility: {portfolio_volatility * 100:.2f}%")

    except Exception as e:
        click.echo(f"Error: {e}")

if __name__ == '__main__':
    cli()
