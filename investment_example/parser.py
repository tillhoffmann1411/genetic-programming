import os
import pandas as pd
from stock import Stock
import random
from datetime import datetime

def load_all_symbols() -> list[str]:
  files = ((x[0], x[2]) for x in os.walk('/Users/tillhoffmann/Projects/uni/heuristic-algorithms/first-deap-test/investment_example/data/stocks'))
  symbols = []
  for file in files:
      for f in file[1]:
        if f != '.DS_Store':
          symbols.append(f.strip('.csv'))
  return symbols

def generate_all_assets(symbols: list, sample: int) -> list[Stock]:
  all_assets = []
  for symbol in random.sample(symbols, sample):
    all_assets.append(Stock(symbol))
  return all_assets

def load_nasdaq_symbols(top: int = 100) -> list[str]:
  sym = pd.read_csv("/Users/tillhoffmann/Projects/uni/heuristic-algorithms/first-deap-test/investment_example/data/nasdaq_largest.csv", usecols=lambda x: x.lower() in ["symbol", "market cap"], index_col=0)
  sym = sym.sort_values(by=["Market Cap"], ascending=False).drop(["Market Cap"], axis=1)
  return sym.index.to_list()[:top]