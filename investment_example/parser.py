import os
import pandas as pd
from stock import Stock
import random
from datetime import datetime

def load_all_symbols() -> list[str]:
  files = ((x[0], x[2]) for x in os.walk('./../data/'))
  symbols = []
  for file in files:
      for f in file[1]:
        if f != '.DS_Store':
          symbols.append(f.strip('.csv'))
  return symbols

def generate_all_assets(symbols: list, sample: int = 10) -> list[Stock]:
  all_assets = []
  for symbol in random.sample(symbols, sample):
    all_assets.append(Stock(symbol))
  return all_assets
