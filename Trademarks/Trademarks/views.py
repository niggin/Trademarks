# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from Trademarks.models import Word
from Trademarks.eng_eng import *

def home(request):
    context = {}
    return render(request, 'index.html', context)

def search(request):
    p = DoubleMetaphon(request.POST['findme']).transcription 
    te = list(Word.objects.filter(ipa__startswith=p))
    p = request.POST['findme'] + ': [' + p + ']'
    context = {'text' : p, 'array' : te}
    return render(request, 'search.html', context)
