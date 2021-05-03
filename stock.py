import pandas as pd

class Stock:
  def __init__(self, sym: str):
    self.data = pd.read_csv('./data/stocks/' + sym + '.csv')
    self.data['Date'] = pd.to_datetime(self.data['Date'])

  def get_avg_profit(from: pd.Timestamp, to: pd.Timestamp):
    diff = to - from
    diff_years = diff / np.timedelta64(1, 'Y')
    if diff_years < 1:
      avg_profit = self.data['Date' == from]