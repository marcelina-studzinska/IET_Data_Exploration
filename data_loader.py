import pandas as pd

COLUMNS = ['iso_code', 'continent', 'location', 'total_cases', 'new_cases', 'total_deaths',
           'new_deaths', 'total_cases_per_million', 'new_cases_per_million', 'total_deaths_per_million',
           'new_deaths_per_million', 'weekly_hosp_admissions', 'weekly_hosp_admissions_per_million',
           'new_tests', 'total_tests', 'total_tests_per_thousand', 'new_tests_per_thousand', 'positive_rate',
           'tests_per_case', 'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated',
           'new_vaccinations', 'total_vaccinations_per_hundred', 'people_vaccinated_per_hundred',
           'people_fully_vaccinated_per_hundred']


def download_whole_data():
    data = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv', index_col='date', parse_dates=True)
    data = data[COLUMNS]
    data.to_csv('covid_data/covid_full.csv')
