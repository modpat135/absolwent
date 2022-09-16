from django.http import HttpResponse

def index(request):
    return HttpResponse("Witaj w Django, juz po tobie")

def info(request):
    return HttpResponse("jestes poszukiwany przez mobbyn<")




