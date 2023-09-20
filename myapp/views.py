from django.shortcuts import render
import waffle


def new_feature_view(request):
    context = {}
    if waffle.flag_is_active(request, 'button'):

        context['show'] = True
    else:
        context['show'] = False

    return render(request, 'simple.html', context)
