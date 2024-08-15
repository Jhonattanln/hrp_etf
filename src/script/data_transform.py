"""Data transform."""
#%% Import libraries
import pandas as pd
from numpy import nan

# %% Import data
etf = pd.read_excel('src/data/etf.xlsx', index_col=0,
                    parse_dates=True, skiprows=3)

# %%
