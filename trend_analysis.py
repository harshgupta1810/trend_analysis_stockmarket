import pandas as pd
import numpy as np
import mplfinance as mpf
import yfinance as yf
from datetime import date
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
import plotly.graph_objects as go

def get_stock_data(ticker_symbol, start_date, end_date):
    """Retrieves historical stock price data for a given ticker symbol from a start date to an end date"""
    ticker = yf.Ticker(ticker_symbol)
    df = ticker.history(interval="1d", start=start_date, end=end_date)
    df.index = pd.to_datetime(df.index, errors='coerce')
    df = df.loc[:,['Open', 'High', 'Low', 'Close']]
    return df

def plot_candlestick_chart(df):
    """Plots a candlestick chart using Plotly"""
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                                          open=df['Open'],
                                          high=df['High'],
                                          low=df['Low'],
                                          close=df['Close'])])
    fig.show()

def get_trend(df):
    """Fits a linear regression model to the closing price data and determines the trend of the stock based on the slope of the regression line"""
    X = df.index.values.reshape(-1, 1)
    y = df['Close'].values.reshape(-1, 1)
    model = LinearRegression().fit(X, y)
    slope = model.coef_[0][0]
    if slope > 0:
        return 'upward'
    elif slope < 0:
        return 'downward'
    else:
        return 'sideways'
