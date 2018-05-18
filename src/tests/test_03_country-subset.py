import importlib

country = importlib.import_module('.data.03_country-subset', 'src')

# you might need to change the date so that it matches today's date
processed_data = "data/processed/2018-05-18-winemag_Chile.csv"
interim_data = "data/interim/2018-05-18-winemag_priceGBP.csv"


def test_get_mean_price():
    mean_price = country.get_mean_price(processed_data)
    assert mean_price == 20.7865
