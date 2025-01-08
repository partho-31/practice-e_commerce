from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def menu(response):
    food_list = ['Apple','Bannana','Jack fruits','Orange']
    return HttpResponse(food_list)