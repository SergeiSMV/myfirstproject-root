from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return HttpResponse('This is about page')



def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['text']
    words = len(user_text.split())
    return render(request, 'reverse.html', {'text': user_text,
                                            'words': words})
