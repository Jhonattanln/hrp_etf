"""Data transform."""

#%% Import libraries
import pandas as pd
from numpy import nan

# %% Class Transform data
class TransformData:
    def __init__(self):
        self.local = '/home/jhonattanln/hrp_etf/src/data/'
        self.file = 'etf.xlsx'

    def extract_data(self):
        etf = pd.read_excel(self.local + self.file, index_col=0,
                            parse_dates=True, skiprows=3)
        global etf
        return etf

    def rename_columns(self):
        et
# %% Call class
if __name__ == '__main__':
    trasform = TransformData()
    data = trasform.extract_data()
    print(data)

# %%
