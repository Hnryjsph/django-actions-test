from django.shortcuts import render



def new_feature_view(request):
    context = {}


    context['show'] = True


    return render(request, 'simple.html', context)
