# CLI Covariance Portfolio Optimizer

In portfolio optimization, the covariance matrix of asset returns is a key input. One can calculate this matrix using historical return data. The covariance matrix is essential for assessing the relationship between assets and for constructing efficient portfolios. In this repository, we develop a CLI to calculate the covariance matrix and optimize portfolios for a custom set of stocks. 

This is an assigned project for MATH2015 (Linear Algebra & Probability) during the Fall 2023 semester. This project is still in development. 

# Installation

Please make sure you have a recent version of Python 3, preferably Python 3.9 or newer. Clone the repository into a local folder and enter the folder:
```
git clone https://github.com/ama2369/CLI-Covariance-Optimizer
cd CLI-Covariance-Optimizer
```

Install required packages in editable mode:

```
pip install -e .
```

To ensure a successful installation, run the following command to graph stock data for a ticker and date range:
```
optimize view 2023-11-13 2023-11-18 AAPL
```

# Usage

Inside the CLI, use --help for an easily accessible description of commands. The date format is always YYYY-MM-DD. 

```
optimize --help
```
### View Command
Graph stock data for a date range and any given number of tickers. 
```
optimize view <start date> <end date> <ticker> 
```
For example, to graph the close prices of Apple, Google, and Microsoft for 2021, run the following command:
```
optimize view 2021-01-01 2022-01-01 AAPL GOOGL MSFT
```
### Covariance Command
Calculate the covariance matrix for a data range with any number of tickers, each separated by a space. 
```
optimize covariance <start date> <end date> <tickers>
```
The output can also be saved to a file in CSV format by passing the --file flag. 
```
optimize covariance --file <filename> <start date> <end date> <tickers>
```

For example, to print the covariance matrix for Apple, Google, and Microsoft for 2021, run the following command:
```
optimize covariance 2021-01-01 2022-01-01 AAPL GOOGL MSFT
```

To save the previous covariance matrix to a file, use the command:
```
optimize covariance --file covariance_matrix.csv 2021-01-01 2022-01-01 AAPL GOOGL MSFT
```

### Weight Command
To find the optimal asset weights for a portfolio, minimizing its variance, use the weight command. The file path should include the covariance matrix in CSV format. 
```
optimize weight <file path>
```
For example, to print the past optimal weights of Apple, Google, and Microsoft in a portfolio, use the following command: 
```
optimize weight covariance_matrix.csv
```

### Returns Command
 Calculate the return of a portfolio for a given time frame, tickers, and weights.
```
optimize returns <start date> <end date> <ticker> <weight>
```
For example, to show the returns and volatility during 2021 for a portfolio evenly consisting of Apple, Google, and Microsoft, run the command:

```
optimize returns 2021-01-01 2022-01-01 AAPL 0.33 GOOGL 0.33 MSFT 0.33
```


### Download Command

To download stock data in CSV format, you can run the following command for any number of tickers. 
```
optimize download <output directory> <start date> <end date> <tickers>
```

For example, to download the stock data for Apple, Google, and Microsoft, use the following command:
```
optimize download . 2021-01-01 2022-01-01 AAPL GOOGL MSFT
```


