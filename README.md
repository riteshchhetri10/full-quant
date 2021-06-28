# full-quant
This repo contains Python implementations of concepts like Modern portfolio theory, CAPM,Black Scholes Option Pricing Model and prediction of stock prices using Monte Carlo Simulation from quantitative finance.

The Bond Pricing Jupyter Notebook is a simple implementation of Zero Coupon Bonds and Coupon Bonds. 
Zero Coupon Bonds pay the entire invested amount and some profit at the maturity.
Coupon Bonds represent interest payments at equal intervals till maturity unlike Zero Coupon Bonds.

Wiener Process or the Brownian motion is an important assumption to model the stock prices. The Wiener Process python implementation involves simply plotting the various datapoints drawn by cumulatively adding a random value from a normal distribution with mean as 0 and variance as dt ( the timestep provided ). The wiener process may result in negative values for the stock values which do not make sense hence paving way for the geometric random walk process.



