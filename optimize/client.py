import click
import yfinance as yf

@click.group()
def cli():
    """Usage: <view> to view data for stock"""
    pass

@cli.command(help='<ticker symbol> <start_date> <end_date>. Date format: <YYYY-MM-DD>. View stock data for a given ticker and date range')
@click.argument('ticker_symbol')
@click.argument('start_date')
@click.argument('end_date')
def view(ticker_symbol, start_date, end_date):
    ticker_data = yf.Ticker(ticker_symbol)
    historical_data = ticker_data.history(start=start_date, end=end_date)
    click.echo(historical_data)

if __name__ == '__main__':
    cli()
