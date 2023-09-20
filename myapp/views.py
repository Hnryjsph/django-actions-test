from django.shortcuts import render
from git import Repo
from django.views.decorators.csrf import csrf_exempt

def new_feature_view(request):
    context = {}


    context['show'] = True


    return render(request, 'simple.html', context)


@csrf_exempt
def webhook(request):

    if request.method == 'POST':
        try:
            repo = Repo('https://github.com/Hnryjsph/django-actions-test.git')
            git = repo.git
            git.pull()
            return "Updated SERVER", 200
        except:
            print("Here")
    else:
        return 'Wrong event type', 400

    return render(request, 'simple.html')


