from django.shortcuts import render

from DEApp.data_loader import COLUMNS_COVID_USABLE, TIMES_COVID, COUNTRIES
from DEApp.covid_draw import draw_covid1, draw_covid2, draw_covid3, get_rank

context = dict()


def index(request):
    context['countries'] = COUNTRIES
    context['measurements'] = COLUMNS_COVID_USABLE
    context['times'] = TIMES_COVID
    context['selected_country'] = 'Poland'
    context['selected_another_country'] = 'Germany'
    context['selected_measurement'] = 'new_cases'
    context['selected_time'] = 'month'
    draw_covid1(context['selected_country'], context['selected_measurement'], context['selected_time'])
    draw_covid2(context['selected_country'], context['selected_another_country'], context['selected_measurement'],
                context['selected_time'])
    draw_covid3(context['selected_country'], context['selected_measurement'], context['selected_time'])
    context['ranking'] = get_rank(context['selected_measurement'])
    return render(request, 'DEApp/DEApp.html', context)


def covid_plot(request):
    if request.method == 'POST':
        context['selected_country'] = request.POST.get("country")
        context['selected_another_country'] = request.POST.get("another_country")
        context['selected_measurement'] = request.POST.get("measurement")
        context['selected_time'] = request.POST.get("time")
    draw_covid1(context['selected_country'], context['selected_measurement'], context['selected_time'])
    draw_covid2(context['selected_country'], context['selected_another_country'], context['selected_measurement'],
                context['selected_time'])
    draw_covid3(context['selected_country'], context['selected_measurement'], context['selected_time'])
    context['ranking'] = get_rank(context['selected_measurement'])
    return render(request, 'DEApp/DEApp.html', context)


def predictions(request):
    # TODO
    return render(request, 'DEApp/Predictions.html', context)


def advanced_analysis(request):
    # TODO
    return render(request, 'DEApp/AdvancedAnalysis.html', context)
