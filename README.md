# full-quant
This repo contains Python implementations of concepts like Modern portfolio theory, CAPM,Black Scholes Option Pricing Model and prediction of stock prices using Monte Carlo Simulation from quantitative finance.
All the datasets for the code implementations are obtained from the yahoofinance servers directly. The yfinance python module helps us to download historical market data quite efficiently.

The Bond Pricing Jupyter Notebook is an implementation of Zero Coupon Bonds and Coupon Bonds present and final value calculations in python. 
Zero Coupon Bonds pay the entire invested amount and some profit at the maturity.
Coupon Bonds represent interest payments at equal intervals till maturity unlike Zero Coupon Bonds.

Wiener Process or the Brownian motion is an important assumption to model the stock prices. The Wiener Process python implementation involves plotting the various datapoints drawn by cumulatively adding a random value from a normal distribution with mean as 0 and variance as dt ( the timestep provided ). The wiener process may result in negative values for the stock values which do not make sense hence paving the way for the geometric random walk process.

Geometric Brownian Motion is a great starting point to model stock prices and predict their values. This is akin to assuming a lognormal distribution for the stock prices.

The Value at Risk Python implementation for the Citigroup stock data for a given timeframe helps us understand the maximum amount of money we may lose from our investment based on a pre-specified confidence interval. The main assumption for this VaR calculation was that the returns are normally distributed.

