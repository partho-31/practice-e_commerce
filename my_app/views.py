from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def menu(request):
    food_list = ['Apple','Bannana','Jack fruits','Orange']
    return HttpResponse(food_list)

def next(request,id):
    return HttpResponse(f'this is a dynamic page {id}')