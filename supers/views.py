from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.
@api_view("GET", "POST")
def supers_list(request):
    pass

@api_view("GET", "PUT", "DELETE")
def supers_detail(request, pk):
    pass