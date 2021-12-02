Stocks = {
"WMT" : 156.68, "MSFT" : 346.91, "GOOGL" : 2822.11, "TWTR" : 48.22, "COIN" : 334.36 ,
"BUD" : 58.56, "V" : 198.94, "NFLX" : 763.90, "TSLA" : 876.44 , "ACER" : 456.43
  }
ticker = input('Enter a ticker symbol for the stock:')

if ticker in Stocks:
  print('{} : {}'.format(ticker, Stocks[ticker]))
else:
  print("The ticker {} was not found".format(ticker))
