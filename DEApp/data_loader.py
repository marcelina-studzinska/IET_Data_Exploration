import pandas as pd

COLUMNS_COVID_USABLE = ['total_cases', 'new_cases', 'total_deaths', 'iso_code',
                        'new_deaths', 'total_cases_per_million', 'new_cases_per_million', 'total_deaths_per_million',
                        'new_deaths_per_million', 'weekly_hosp_admissions', 'weekly_hosp_admissions_per_million',
                        'new_tests', 'total_tests', 'total_tests_per_thousand', 'new_tests_per_thousand',
                        'positive_rate',
                        'tests_per_case', 'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated',
                        'new_vaccinations', 'total_vaccinations_per_hundred', 'people_vaccinated_per_hundred',
                        'people_fully_vaccinated_per_hundred']
COLUMNS_COVID = COLUMNS_COVID_USABLE + ['location']
TIMES_COVID = ['week', 'month', '3 months', '6 months', 'all']
COUNTRIES = []
GROUPS = ['World', 'Europe', 'Asia', 'North America', 'European Union', 'South America', 'Africa']
COVID_DATA = None
CURRENCY_CODES = None


# def read_table_with_tickers():
#     df_names = pd.read_excel('data/yahoo_data.xlsx')
#     df_names = df_names.dropna()
#     return df_names
#
#
# def is_ticker_possible(df_names, str_name):
#     ticker_list = df_names[df_names["Name"].str.contains(str_name)]["Ticker"].tolist()
#     if len(ticker_list) > 0:
#         return True
#     else:
#         return False
#
#
# def check_date(value, min_val, max_val):
#     """
#     :param value: wartość pola
#     :param min_val: minimalna dopuszczalna wartość (włącznie)
#     :param max_val: maksymalna dopuszczalna wartość (włącznie)
#     :return: True - jeśli wartosć jest poprawna / False - jęsli wartość jest niepoprawna
#     """
#     value = str(value)
#     if value.isdecimal():
#         value = int(value)
#         if value >= min_val and value <= max_val:
#             return True
#         else:
#             return False
#     else:
#         return False
#
#
# def return_valid_date(value):
#     """
#     Używane do odpowiedniego formatowania wartości w dacie
#     np. 1 -> '01'
#     :param value: wartość
#     :return: wartość jako string i długości 2
#     """
#     value = str(value)
#     if len(value) == 1:
#         value = '0' + value
#         return value
#     else:
#         return value
#
#
# def get_stock_data(df_names, long_name, year, month, day):
#     if is_ticker_possible(df_names, long_name):
#         name = find_ticker_list(df_names, long_name)[0]
#         if check_date(year, 2000, 2021) and check_date(month, 1, 12) and check_date(day, 1, 31):
#             year, month, day = str(year), return_valid_date(month), return_valid_date(day)
#             string_data = "{0}-{1}-{2}".format(str(year), str(month), str(day))
#             df = yf.download(name, start=string_data)
#             return df

# Covid
def download_whole_covid_data():
    data = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv', index_col='date', parse_dates=True)
    data = data[COLUMNS_COVID]
    global COUNTRIES
    COUNTRIES = sorted(list(set(data['location'])))
#     data.to_csv('data/covid_full.csv')
    global COVID_DATA
    COVID_DATA = data


# Currency
def load_currency_code():
    currs = pd.read_excel('data/currency_code.xls', skiprows=3)
    currs['ENTITY'] = currs['ENTITY'].apply(lambda x: x.title())
    currs = currs[['ENTITY', 'Alphabetic Code']]
    currs.set_index('ENTITY', inplace=True)
    global CURRENCY_CODES
    CURRENCY_CODES = currs['Alphabetic Code']


def download_whole_data():
    download_whole_covid_data()
    # load_currency_code()
