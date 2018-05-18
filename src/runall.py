import recipy
import importlib
import datetime

# import modules
subset = importlib.import_module('.data.01_subset-data-GBP', 'src')
plotwines = importlib.import_module('.visualization.02_visualize-wines', 'src')
country_sub = importlib.import_module('.data.03_country-subset', 'src')

#set raw data
raw_data = 'data/raw/winemag-data-130k-v2.csv'

#set country
country = "Chile"

if __name__ == '__main__':
    price_gbp_file = subset.process_data_GBP(raw_data)
    print(price_gbp_file)
    plotwines.create_plots(price_gbp_file)
    country_file = country_sub.get_country(price_gbp_file, country)
    print(country_file)
