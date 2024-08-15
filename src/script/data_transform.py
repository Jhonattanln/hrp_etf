"""Data transform."""

#%% Import libraries
import pandas as pd
from numpy import nan

# %% Class Transform data
class TransformData:
    def __init__(self):
        self.local = '/home/jhonattanln/hrp_etf/src/data/'
        self.file = 'etf.xlsx'
        self.etf = None

    def extract_data(self):
        self.etf = pd.read_excel(self.local + self.file, index_col=0,
                            parse_dates=True, skiprows=3)
        return self.etf

    def rename_columns(self):
        self.etf.columns = self.etf.columns.str[-6:]
        return self.etf

    def replace_null(self):
        self.etf.replace.str('-', nan, inplace=True)
        return self.etf
# %% Call class
if __name__ == '__main__':
    trasform = TransformData()
    data = trasform.extract_data()
    columns = trasform.rename_columns()
    replace = trasform.rename_columns()
    print(data.head())

# %%
