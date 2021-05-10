from typing import Dict
from stock import Stock
from datetime import datetime
import random

def profit10(asset: Stock, hold1: int, hold2: int) -> int:
  return profit_larger(asset, min_profit=0.1, hold1=hold1, hold2=hold2)

def profit20(asset: Stock, hold1: int, hold2: int) -> int:
  return profit_larger(asset, min_profit=0.2, hold1=hold1, hold2=hold2)

def profit40(asset: Stock, hold1: int, hold2: int) -> int:
  return profit_larger(asset, min_profit=0.4, hold1=hold1, hold2=hold2)

def profit60(asset: Stock, hold1: int, hold2: int) -> int:
  return profit_larger(asset, min_profit=0.6, hold1=hold1, hold2=hold2)

def profit80(asset: Stock, hold1: int, hold2: int) -> int:
  return profit_larger(asset, min_profit=0.8, hold1=hold1, hold2=hold2)

def profit_larger(asset: Stock, min_profit: float, hold1: int, hold2: int) -> int:
  profit = asset.get_avg_profit(end=datetime(2015, 1, 23))
  if profit is not None and profit > min_profit:
    return hold1
  else:
    return hold2



def risk10(asset: Stock, hold1: int, hold2: int) -> int:
  return risk_larger(asset, min_risk=0.1, hold1=hold1, hold2=hold2)

def risk20(asset: Stock, hold1: int, hold2: int) -> int:
  return risk_larger(asset, min_risk=0.2, hold1=hold1, hold2=hold2)

def risk40(asset: Stock, hold1: int, hold2: int) -> int:
  return risk_larger(asset, min_risk=0.4, hold1=hold1, hold2=hold2)

def risk60(asset: Stock, hold1: int, hold2: int) -> int:
  return risk_larger(asset, min_risk=0.6, hold1=hold1, hold2=hold2)

def risk80(asset: Stock, hold1: int, hold2: int) -> int:
  return risk_larger(asset, min_risk=0.8, hold1=hold1, hold2=hold2)

def risk_larger(asset: Stock, min_risk: float, hold1: int, hold2: int) -> int:
  risk = asset.get_avg_risk(end=datetime(2015, 1, 23))
  if risk is not None and risk > min_risk:
    return hold1
  else:
    return hold2


def stock(asset: Stock) -> Stock:
  return asset


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

def get_cor_from_stocks(stock1: Stock, stock2: Stock, start: datetime = 0, end: datetime = 0):
  stock1_filtered = stock1.get_data_between(start, end)['Close']
  stock2_filtered = stock2.get_data_between(start, end)['Close']
  return stock1_filtered.corr(stock2_filtered)

def get_random_sym(symbols: list[str], seed: int = None):
  random.seed(seed)
  rand_i = random.randint(0, len(symbols))
  return symbols[rand_i]

def get_seed():
  return random.randint(0, 999999)