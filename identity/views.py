from django.shortcuts import render
from .models import person

# Create your views here.
def index(request):
    context = {"person": person.objects.all()}
    return render(request, 'index.html', context)