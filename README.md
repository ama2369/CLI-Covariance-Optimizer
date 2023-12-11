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

To ensure a successful installation, run the following command to view stock data for a ticker and date range:
```
optimize view AAPL 2023-11-13 2023-11-18
```

# Usage

Inside the CLI, use --help for an easily accessible description of commands. The date format is always YYYY-MM-DD. 

```
optimize --help
```

View stock data for a given ticker and date range.
```
optimize view <ticker symbol> <start date> <end date>
```

Calculate the covariance matrix for a data range with any number of tickers, each separated by a space. 
```
optimize covariance <start date> <end date> <tickers>
```

Custom data from a file in CSV format can also be used as input with the --file flag. The file must contain columns named in the format "Adj Close \<Ticker>". 
```
optimize covariance --file <file path>
```

To download a file in CSV format, you can run the following command for any number of tickers. 
```
optimize download <output directory> <start date> <end date> <tickers>
```


