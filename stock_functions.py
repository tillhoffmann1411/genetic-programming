import os
import pandas as pd
from stock import Stock
import random
from datetime import datetime



def sell(stocks: list, index: int = 0):
  index = random.randint(0, len(stocks))
  try:
    del stocks[index-1]
    return stocks
  except:
    return stocks
    

def buy(stocks: list, seed: int):
  sym = get_random_sym(seed)
  stocks.append(Stock(sym))
  return stocks

def get_all_symbols():
  files = ((x[0], x[2]) for x in os.walk('./data/'))
  symbols = []
  for file in files:
      for f in file[1]:
          if f != '.DS_Store':
              symbols.append(f.strip('.csv'))
  symbols.sort()
  return symbols

def get_num_assets():
  return len(all_sym)

def get_cor_from_stocks(stock1: Stock, stock2: Stock, start: datetime = 0, end: datetime = 0):
  stock1_filtered = stock1.get_data_between(start, end)['Close']
  stock2_filtered = stock2.get_data_between(start, end)['Close']
  return stock1_filtered.corr(stock2_filtered)

def get_random_sym(seed: int = None):
  random.seed(seed)
  rand_i = random.randint(0, len(all_sym))
  return all_sym[rand_i]

def get_seed():
  return random.randint(0, 999999)


all_sym = get_all_symbols()
