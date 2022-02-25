from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')
    
def player_entry(request):
    return render(request, 'home/player_entry', {'title': 'Player Entry'})