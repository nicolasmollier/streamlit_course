"""
# My first app
Here's our first attempt at using data to create a table:
"""

import yfinance as yf
import streamlit as st
import pandas as pd

ticker_symbol = "AAPL"

st.write(f"""
# Simple Stock Price App

Shown are the stock closing price and volume of {ticker_symbol}!
""")


ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period="1d", start="2007-01-01", end="2022-11-26")
st.line_chart(ticker_df.Close)