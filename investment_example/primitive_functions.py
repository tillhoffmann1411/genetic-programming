from typing import Dict
from stock import Stock
from datetime import datetime
import random

def profit10(asset: Stock, hold1: int, hold2: int) -> int:
  return profit_larger(asset, min_profit=0.1, hold1=hold1, hold2=hold2)

def profit20(asset: Stock, hold1: int, hold2: int) -> int:
  return profit_larger(asset, min_profit=0.2, hold1=hold1, hold2=hold2)

def profit30(asset: Stock, hold1: int, hold2: int) -> int:
  return profit_larger(asset, min_profit=0.3, hold1=hold1, hold2=hold2)

def profit40(asset: Stock, hold1: int, hold2: int) -> int:
  return profit_larger(asset, min_profit=0.4, hold1=hold1, hold2=hold2)

def profit50(asset: Stock, hold1: int, hold2: int) -> int:
  return profit_larger(asset, min_profit=0.5, hold1=hold1, hold2=hold2)

def profit60(asset: Stock, hold1: int, hold2: int) -> int:
  return profit_larger(asset, min_profit=0.6, hold1=hold1, hold2=hold2)

def profit70(asset: Stock, hold1: int, hold2: int) -> int:
  return profit_larger(asset, min_profit=0.7, hold1=hold1, hold2=hold2)

def profit80(asset: Stock, hold1: int, hold2: int) -> int:
  return profit_larger(asset, min_profit=0.8, hold1=hold1, hold2=hold2)

def profit90(asset: Stock, hold1: int, hold2: int) -> int:
  return profit_larger(asset, min_profit=0.9, hold1=hold1, hold2=hold2)

def profit_larger(asset: Stock, min_profit: float, hold1: int, hold2: int) -> int:
  profit = asset.get_avg_profit(end=datetime(2015, 1, 1))
  if profit is not None and profit > min_profit:
    return hold1
  else:
    return hold2



def risk10(asset: Stock, hold1: int, hold2: int) -> int:
  return risk_larger(asset, min_risk=0.1, hold1=hold1, hold2=hold2)

def risk20(asset: Stock, hold1: int, hold2: int) -> int:
  return risk_larger(asset, min_risk=0.2, hold1=hold1, hold2=hold2)

def risk30(asset: Stock, hold1: int, hold2: int) -> int:
  return risk_larger(asset, min_risk=0.3, hold1=hold1, hold2=hold2)

def risk40(asset: Stock, hold1: int, hold2: int) -> int:
  return risk_larger(asset, min_risk=0.4, hold1=hold1, hold2=hold2)

def risk50(asset: Stock, hold1: int, hold2: int) -> int:
  return risk_larger(asset, min_risk=0.5, hold1=hold1, hold2=hold2)

def risk60(asset: Stock, hold1: int, hold2: int) -> int:
  return risk_larger(asset, min_risk=0.6, hold1=hold1, hold2=hold2)

def risk70(asset: Stock, hold1: int, hold2: int) -> int:
  return risk_larger(asset, min_risk=0.7, hold1=hold1, hold2=hold2)

def risk80(asset: Stock, hold1: int, hold2: int) -> int:
  return risk_larger(asset, min_risk=0.8, hold1=hold1, hold2=hold2)

def risk90(asset: Stock, hold1: int, hold2: int) -> int:
  return risk_larger(asset, min_risk=0.9, hold1=hold1, hold2=hold2)

def risk_larger(asset: Stock, min_risk: float, hold1: int, hold2: int) -> int:
  risk = asset.get_avg_risk(end=datetime(2015, 1, 1))
  if risk is not None and risk > min_risk:
    return hold1
  else:
    return hold2


def stock(asset: Stock) -> Stock:
  return asset