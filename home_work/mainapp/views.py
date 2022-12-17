from django.shortcuts import render

from mainapp.models import Person


def index(request):
    people = Person.objects.all()
    print(people.query)
    estimation = people.filter(estimation="5")
    print(estimation.query)
    context = {
        'people': people,
        'estimation': estimation,
    }
    return render(request, 'mainapp/index.html', context)
