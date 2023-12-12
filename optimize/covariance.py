import numpy as np
from scipy.optimize import minimize

def calculate_covariance(stock_data):
    returns = stock_data.pct_change().dropna()
    covariance_matrix = returns.cov()
    return covariance_matrix

#Find the optimal asset weights for a portfolio, minimizing its variance
def optimize_weights(matrix):
    n = len(matrix)

    #The sum of the weights must equal 1
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})

    #Each weight is between 0 and 1
    bounds = tuple((0, 1) for asset in range(n))

    #Calculate the portfolio variance
    def portfolio_variance(weights):
        return np.dot(weights.T, np.dot(matrix, weights))
    
    init_guess = np.full(n, 1/n)

    #Minimize the portfolio_variance function 
    opt_results = minimize(portfolio_variance, init_guess, method='SLSQP', bounds=bounds, constraints=constraints)

    return opt_results.x
