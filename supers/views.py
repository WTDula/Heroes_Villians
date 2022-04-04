from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Super
from .serializers import SuperSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.
@api_view(["GET", "POST"])
def supers_list(request):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        serializer = SuperSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def supers_detail(request, pk):
    super = get_object_or_404(Super, pk = pk)
    if request.method == "GET":
        serializer = SuperSerializer(super)
        return Response(serializer.data)
    