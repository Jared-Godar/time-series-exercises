import pandas as pd
from datetime import timedelta, datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

import warnings
warnings.filterwarnings("ignore")

from acquire import get_store_data

# plotting defaults
plt.rc('figure', figsize=(13, 7))
plt.style.use('seaborn-whitegrid')
plt.rc('font', size=16)


######### PREPARE STORE DATA ##############

def prepare():
    '''
    This function acquires store data, converts datetime, reindexed on date, and adds engineered columns.
    '''
    df = get_store_data()
    print('Data acquired...')
    print('Converting to datetime')
    df.sale_date = pd.to_datetime(df.sale_date)
    df = df.set_index("sale_date").sort_index()
    print('Sale date set to datetime and reindexed...')
    df['month'] = df.index.month
    df['weekday'] = df.index.day_name()
    df['sales_total']=df.sale_amount * df.item_price
    print('Added engineered columns...')
    print('Prepare complete')
    return df

########## PREPARE POWER DATA #########################

def prepare2(): 
    df = pd.read_csv("https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv")
    print('Read power data from CSV...')
    print('Converting date to datetime...')
    df.Date = pd.to_datetime(df.Date)
    df = df.set_index("Date").sort_index()
    print('Dates converted and reindexed...')
    df['month'] = df.index.month
    df['year'] = df.index.year
    print('Added engineered columns...')
    print('Filling NAs...')
    df.ffill(inplace=True)
    df.bfill(inplace=True)
    print('Null value counts:')
    print(df.isnull().sum())
    print('Data prep complete.')
    return df


######