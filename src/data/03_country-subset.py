#!/usr/bin/env python


import sys
import datetime

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def get_country(filename, country):
    """
    Do a simple analysis per country
    Args:
    -----
    filename: str
        Path to the filename containing the wine data
    country: str
        Country to be used to subset

    Returns:
    -----
    fname: st
        Path to the created data set
    """

    # Load table
    wine = pd.read_csv(filename)

    # Use the country name to subset data
    subset_country = wine[wine['country'] == country ].copy()

    # Subset the

    # Constructing the fname
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    fname = f'data/processed/{today}-winemag_{country}.csv'

    # Saving the csv
    subset_country.to_csv(fname)

    return(fname)


def get_mean_price(filename):
    """Compute the mean price of wines
    Args:
    -----
    filename: str
        Path to the filename containing the wine data
    
    Returns:
    -----
    mean_price: float
        Mean price computed from the subset data
    """  
    wine = pd.read_csv(filename)
    mean_price = wine['price'].mean()
    return round(mean_price, 4)


if __name__ == '__main__':
    filename = sys.argv[1]
    country = sys.argv[2]
    print(f'Subsetting: {filename}')
    print(f'Country searched: {country}')

    print(get_country(filename, country))
