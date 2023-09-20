from django.shortcuts import render
import git

def new_feature_view(request):
    context = {}


    context['show'] = True


    return render(request, 'simple.html', context)

def webhook(request):
    if request.method == 'POST':
        repo = git.Repo('https://github.com/Hnryjsph/django-actions-test.git')
        origin = repo.remotes.origin
        origin.pull()
        return "Updated SERVER", 200
    else:
        return 'Wrong event type', 400


