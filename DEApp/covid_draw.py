from datetime import timedelta, datetime
from matplotlib.dates import DateFormatter
import matplotlib.pyplot as plt
from dateutil.relativedelta import relativedelta

from DEApp.currency_code import get_currencies
from DEApp.data_loader import COVID_DATA, GROUPS, CURRENCY_CODES


def prepare_covid_data(time):
    data = COVID_DATA
    today = datetime.now()
    time_prior = today - timedelta(days=1)
    if time == 'week':
        time_prior = today - timedelta(weeks=1)
    elif time == 'month':
        time_prior = today - relativedelta(months=1)
    elif time == '3 months':
        time_prior = today - relativedelta(months=3)
    elif time == '6 months':
        time_prior = today - relativedelta(months=6)
    elif time == 'all':
        time_prior = data.index[0]
    data = data[data.index >= time_prior]
    return data, time_prior


def draw_covid1(country, measure, time):
    """
    Prepare basic plot.
    :param country: str country name
    :param measure: str measurement to be plotted
    :param time: str time range for plot
    """
    data, time_prior = prepare_covid_data(time)
    data = data[data['location'] == country]
    plt.rcParams.update({'font.size': 20})
    fig, ax = plt.subplots(figsize=(20, 8))
    ax.set_xlim([time_prior, datetime.now()])
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    ax.plot(data[measure].rolling(window='3d').mean(), 'y-', linewidth=8, label='running average (3 days)')
    ax.plot(data[measure].rolling(window='7d').mean(), 'g-', linewidth=8, label='running average (week)')
    ax.plot(data[measure], 'r.-', markersize=25, linewidth=3)
    ax.grid()
    plt.xticks(rotation=30,)
    plt.title(measure + " in " + country, fontdict={'fontsize': 40, 'color': "white"})
    plt.legend()
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_fontsize(30)
    ax.yaxis.label.set_fontsize(30)
    ax.tick_params(colors='white')
    fig.savefig('static/images/covid1.png', dpi=300, bbox_inches='tight', transparent=True)
    fig.clf()


def draw_covid2(country1, country2, measure, time):
    """
    Prepare basic plot.
    :param country1: str country name
    :param country2: str another country name
    :param measure: str measurement to be plotted
    :param time: str time range for plot
    """
    data, time_prior = prepare_covid_data(time)
    data1 = data[data['location'] == country1]
    data2 = data[data['location'] == country2]
    plt.rcParams.update({'font.size': 20})
    fig, ax = plt.subplots(figsize=(20, 8))
    ax.set_xlim([time_prior, datetime.now()])
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    ax.plot(data1[measure], 'r.-', markersize=25, label=country1, linewidth=3)
    ax.plot(data2[measure], 'y.-', markersize=25, label=country2, linewidth=3)
    ax.grid()
    plt.xticks(rotation=30,)
    plt.title(measure + " in " + country1 + " and " + country2, fontdict={'fontsize': 40, 'color': "white"})
    plt.legend()
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_fontsize(30)
    ax.yaxis.label.set_fontsize(30)
    ax.tick_params(colors='white')
    fig.savefig('static/images/covid2.png', dpi=300, bbox_inches='tight', transparent=True)
    fig.clf()


def get_rank(measure):
    """
    Prepare basic plot.
    :param measure: str measurement to be plotted
    """
    data = COVID_DATA
    time = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    time = time - timedelta(hours=24)
    data = data[data.index == time]
    data = data[~data.location.isin(GROUPS)]
    ranking = data.sort_values(measure, ascending=False)[['location', measure]]
    ranking.set_index('location', inplace=True)
    fig, ax = plt.subplots(figsize=(20, 8))
    ax.bar(ranking[:5].index, ranking[:5][measure].values)
    plt.xticks(rotation=30, )
    plt.title("Top 5 " + measure, fontdict={'fontsize': 40, 'color': "white"})
    plt.legend()
    ax.set_ylabel(measure)
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_fontsize(30)
    ax.yaxis.label.set_fontsize(30)
    ax.tick_params(colors='white')
    fig.savefig('static/images/covid3.png', dpi=300, bbox_inches='tight', transparent=True)
    fig.clf()


def draw_covid_shares(country, measure, time):
    """
    Prepare basic plot.
    :param country: str country name
    :param measure: str measurement to be plotted
    :param time: str time range for plot
    """
    data, time_prior = prepare_covid_data(time)
    data = data[data['location'] == country]
    plt.rcParams.update({'font.size': 20})
    fig, ax = plt.subplots(figsize=(20, 8))
    ax.hist(data[measure], density=True, color='red', edgecolor='black')
    plt.xticks(rotation=30,)
    plt.title(measure + " in " + country + " histogram", fontdict={'fontsize': 40, 'color': "white"})
    plt.legend()
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_fontsize(30)
    ax.yaxis.label.set_fontsize(30)
    ax.tick_params(colors='white')
    fig.savefig('static/images/covid4.png', dpi=300, bbox_inches='tight', transparent=True)
    fig.clf()


def draw_covid_currency(country1, country2, measure, time):
    """
    Prepare basic plot.
    :param country1: str country name
    :param country2: str another country name
    :param measure: str measurement to be plotted
    :param time: str time range for plot
    """
    data, time_prior = prepare_covid_data(time)
    data1 = data[data['location'] == country1]
    data2 = data[data['location'] == country2]
    plt.rcParams.update({'font.size': 20})
    fig, ax = plt.subplots(figsize=(20, 8))
    ax.set_xlim([time_prior, datetime.now()])
    currency = get_currencies(country1, country2, str(time_prior)[:10], str(datetime.now())[:10])
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    ax.plot(data1[measure], 'r.-', markersize=25, label=country1, linewidth=3)
    ax.plot(data2[measure], 'y.-', markersize=25, label=country2, linewidth=3)
    ax2 = ax.twinx()
    ax2.plot(currency, 'go-', markersize=25, label=CURRENCY_CODES[country1] + ' to ' +\
             CURRENCY_CODES[country2], linewidth=8)
    ax.grid()
    plt.xticks(rotation=30, )
    plt.title(measure + " and currencies " + " in " + country1 + " and " + country2, fontdict={'fontsize': 40, 'color': "white"})
    plt.legend()
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax2.xaxis.label.set_color('white')
    ax2.yaxis.label.set_color('white')
    ax.xaxis.label.set_fontsize(30)
    ax.yaxis.label.set_fontsize(30)
    ax.tick_params(colors='white')
    ax2.tick_params(colors='white')
    fig.savefig('static/images/covid4.png', dpi=300, bbox_inches='tight', transparent=True)
    fig.clf()
