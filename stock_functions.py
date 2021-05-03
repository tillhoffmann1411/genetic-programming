import os
import pandas as pd
from stock import Stock
import random

def sell(stocks: pd.Series, index: int):
  return stocks.drop([index])

def buy_random(stocks: pd.Series):
  symbols = get_all_symbols()
  rand_i = random.randint(0, len(symbols))
  stocks.add(Stock(symbols[rand_i]))
  return stocks

def get_all_symbols():
  files = ((x[0], x[2]) for x in os.walk('./data/'))
  symbols = []
  for file in files:
      for f in file[1]:
          if f != '.DS_Store':
              symbols.append(f.strip('.csv'))
  return symbols.sort()