from datetime import datetime
import pandas as pd
import numpy as np
import os.path
from enum import Enum


class Asset_Type(Enum):
    STOCK = "stock"
    ETF = "etf"


class Stock:
    def __init__(self, sym: str):
        self.symbol = sym
        if os.path.isfile('./data/stocks/' + sym + '.csv'):
            self.asset_type = 'stock'
            self.data = self._read_data(Asset_Type.STOCK, sym)

        elif os.path.isfile('./data/etfs/' + sym + '.csv'):
            self.asset_type = "etf"
            self.data = self._read_data(Asset_Type.ETF, sym)

        else:
            raise FileNotFoundError(
                "The file " + sym + ".csv does not exists in the ./data folder")

        self.data.index = pd.DatetimeIndex(self.data.index)

    def _read_data(self, kind: Asset_Type, sym: str):
        return pd.read_csv("./data/" + kind.value + "s/" + sym + ".csv", usecols=lambda x: x.lower() in ["date", "close"], index_col=0)

    def get_avg_profit(self, start: datetime = 0, end: datetime = 0):
        filtered_data = self.get_data_between(start, end)
        returns = filtered_data.resample('Y').ffill().pct_change().mean()
        returns = returns.to_frame()
        returns.columns = ['avg_return']
        return returns.iloc[0][0]

    def get_avg_risk(self, start: datetime = 0, end: datetime = 0):
        filtered_data = self.get_data_between(start, end)
        std_data = filtered_data.resample('D').ffill().pct_change()
        std_data = std_data.iloc[1:, :]
        # 252 trayding day in a year
        cov = std_data.cov() * 252
        return cov

    def get_data_between(self, start: datetime = 0, end: datetime = 0):
        if start != 0 and end != 0:
            return self.data[(self.data.index > start) & (self.data.index < end)]
        elif start == 0 and end != 0:
            return self.data[self.data.index < end]
        elif start != 0 and end == 0:
            return self.data[self.data.index > start]
        else:
            return self.data

    def get_data(self):
        return self.data

    def get_symbol(self):
      return self.symbol


# # calculate std
# std_data = data_filter.resample('D').ffill().pct_change()
# std_data = std_data.iloc[1:, :]
# cov = std_data.cov() * 252
