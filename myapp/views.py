from django.shortcuts import render
import waffle
from waffle.decorators import waffle_flag
from waffle.models import Flag

flag, created = Flag.objects.get_or_create(name='new_feature', defaults={'everyone': True})


@waffle_flag('new_feature')
def new_feature_view(request):
    context = {}
    if waffle.flag_is_active(request, 'button'):

        context['show'] = True
    else:
        context['show'] = False

    return render(request, 'simple.html', context)
