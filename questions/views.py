from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

QUESTIONS = [
    {
        'id': i,
        'title': f'Question title {i}',
        'text': f'Text {i}',
    }
    
    for i in range(30)
]
 
def paginate(objects_list, request, per_page=10):
    # Получаем номер страницы из параметров запроса (?page=2)
    page_num = request.GET.get('page', 1)
    paginator = Paginator(objects_list, per_page)
    
    try:
        page = paginator.page(page_num)
    except PageNotAnInteger:
        # Если page не число, показываем первую страницу
        page = paginator.page(1)
    except EmptyPage:
        # Если страница за пределами диапазона, показываем последнюю
        page = paginator.page(paginator.num_pages)
        
    return page

   

def index(request):
    page_obj = paginate(QUESTIONS, request, per_page=5)
    return render( request, "questions/index.html", context= {'questions': page_obj})

def ask(request):
    return render(request, "questions/ask.html")

def login(request):
    return render( request, "questions/login.html")

def profile(request):
    return render(request, "questions/profile.html")

def question(request):
    return render( request, "questions/question.html", context= {'questions': QUESTIONS})

def signup(request):
    return render(request, "questions/signup.html")
def hot(request):
    page_obj = paginate(QUESTIONS, request, per_page=5)
    return render(request, "questions/hot.html", context= {'questions': page_obj[::-1]})
