from django.shortcuts import render
from django.http import HttpResponse

QUESTIONS = [
    {
        'id': i,
        'title': f'Question title {i}',
        'text': f'Text {i}',
    }
    
    for i in range(30)
]

def index(request):
    return render( request, "questions/index.html", context= {'questions': QUESTIONS})

def ask(request):
    return render(request, "questions/ask.html")
