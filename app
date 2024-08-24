import yfinance as yf
import pandas as pd

def fetch_data(ticker):
    data = yf.download(ticker, period="1y", interval="1d")
    return data

nas100_data = fetch_data('^NDX')
