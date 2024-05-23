import yfinance

a = "NVDA"

t = yfinance.Ticker("NVDA")
stock = t.history(period = '5d')
print(stock)