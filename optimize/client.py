import click
import yfinance as yf
from .covariance import calculate_covariance
import os
import pandas as pd

@click.group()
def cli():
    pass

@cli.command(help='<ticker symbol> <start date> <end date>. Date format: <YYYY-MM-DD>. View stock data for a given ticker and date range')
@click.argument('ticker_symbol')
@click.argument('start_date')
@click.argument('end_date')
def view(ticker_symbol, start_date, end_date):
    ticker_data = yf.Ticker(ticker_symbol)
    historical_data = ticker_data.history(start=start_date, end=end_date)
    click.echo(historical_data)

@cli.command(help='<start date> <end date> <tickers>. Use --file <file path> to extract data from a file. Calculate the covariance matrix from a CSV file or using ticker symbols and date range.')
@click.option('--file', 'file_path', type=str, help='Path to the CSV file containing stock data')
@click.argument('start_date', required=False, type=str)
@click.argument('end_date', required=False, type=str)
@click.argument('tickers', nargs=-1)
def covariance(file_path, start_date, end_date, tickers):
    try:
        if file_path:
            if not os.path.exists(file_path):
                click.echo(f'File not found: {file_path}')
                return

            stock_data = pd.read_csv(file_path, index_col='Date')
            
            #Select only the adjusted closing price columns for each ticker
            adj_close_columns = [col for col in stock_data.columns if 'Adj Close' in col]
            stock_data = stock_data[adj_close_columns]
            
            #Rename columns to ticker symbols
            stock_data.columns = [col.replace('Adj Close ', '') for col in stock_data.columns]

        else:
            # Fetch data using yfinance
            if not tickers:
                click.echo('Please provide ticker symbols')
                return

            if not start_date or not end_date:
                click.echo('Please provide start and end dates')
                return

            stock_data = yf.download(list(tickers), start=start_date, end=end_date)['Adj Close']

        #Calculate and print covariance matrix
        covariance_matrix = calculate_covariance(stock_data)
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

    # Convert columns into strings
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = [' '.join(col).strip() for col in data.columns.values]

    # Convert timestamps to string for CSV format
    data.reset_index(inplace=True)
    data['Date'] = data['Date'].dt.strftime('%Y-%m-%d')

    filename = os.path.join(directory, 'stock_data.csv')

    data.to_csv(filename, index=False)

    click.echo(f'Stock data saved to {filename}')
    
if __name__ == '__main__':
    cli()
