from django.shortcuts import render
from webapp.cat import Cat
from django.http import HttpResponseRedirect


# Create your views here.
def index_views(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        Cat.name = request.POST.get('cat_name')
        return HttpResponseRedirect('/cat_stats')


def cat_stats_views(request):
    if request.method == 'GET':
        context = {
                   'name': Cat.name,
                   'age': Cat.age,
                   'satiety': Cat.satiety,
                   'happiness': Cat.happiness,
                   'avatar': Cat.avatar
        }
        return render(request, 'cat_stats.html', context)
    elif request.method == 'POST':
        action = request.POST.get('action')
        if action == 'play':
            Cat.play()
        elif action == 'feed':
            Cat.feed()
        return HttpResponseRedirect('/cat_stats')





