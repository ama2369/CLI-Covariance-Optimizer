# CLI Covariance Portfolio Optimizer

In portfolio optimization, the covariance matrix of asset returns is a key input. One can calculate this matrix using historical return data. The covariance matrix is essential for assessing the relationship between assets and for constructing efficient portfolios. In this repository, we develop a CLI to calculate the covariance matrix and optimize portfolios for a custom set of stocks. 

# Installation

Please make sure you have a recent version of Python 3, preferably Python 3.9 or newer. Clone the repository into a local folder and enter the folder:
```
git clone https://github.com/irtlab/CLI-Covariance-Optimizer
cd CLI-Covariance-Optimizer
```

Install required packages in editable mode:

```
pip install -e .
```

To ensure a successful installation, run the following command to view stock data for a ticker and date range:
```
optimize ticker AAPL 2023-11-13 2023-11-18
```

# Usage

Inside the CLI, use --help for an easily accessible description of commands. 

```
optimize --help
```

View stock data for a given ticker and date range. Date format: <YYYY-MM-DD>. 
```
optimize ticker <ticker symbol> <start_date> <end_date>
```
