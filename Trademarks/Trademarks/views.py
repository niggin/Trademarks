# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from Trademarks.models import Word
from Trademarks.eng_eng import *
from multiprocessing import Process, Queue
import time
import Trademarks.eng_eng

def home(request):
    context = {}
    """f = open("c:/users/rubik_000/documents/base.txt")
    lines = f.read().split('\n')
    for i in range(len(lines)):
        to = lines[i].split('@')
        if len(to) > 1:
            res = DoubleMetaphon(to[0]).transcription
            Word.objects.create(word=to[0],meaning=to[1],ipa=res)
    f.close()"""

    return render(request, 'index.html', context)

def search(request):
    p = DoubleMetaphon(request.POST['findme']).transcription 
    te = list(Word.objects.filter(ipa__contains = p))
    p = request.POST['findme'] + ': [' + p + ']'
    context = {'text' : p, 'array' : te}
    return render(request, 'search.html', context)
