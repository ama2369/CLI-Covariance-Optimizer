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

# Usage

- allow the user to input timeframe to consider historical return data (1, 3, 5 years etc)
- allow the user to input any number of stocks (within reason, will probably edit this later)
- the cli interface automatically gets the historical data for the stocks, but also allows the user to input their own historical data
- the cli interface will output the covariance matrix calculation and also the proposed portfolio optimization (this part of the implementation will depend on Nancy and Tanis code)
