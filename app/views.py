from django.shortcuts import render
from django.http import HttpResponse

def hai(request):
    return HttpResponse('this is changed if address')
    
