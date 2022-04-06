from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from super_types.models import SuperType
from .models import Power, Super
from .serializers import SuperSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.
@api_view(["GET", "POST"])
def supers_list(request):
    if request.method == "GET":
        type_param = request.query_params.get('type')
        
        super = Super.objects.all()
        if type_param:
            super = super.filter(super_type__type = type_param)
            serializer = SuperSerializer(super, many = True)
            return Response(serializer.data)
        else:
            super_types = SuperType.objects.all()
            custom_response_dictionary = {}
            for super_type in super_types:
                super = Super.objects.filter(super_type__id = super_type.id)
                super_serializer = SuperSerializer(super, many = True)
                if super_type.type == "Hero":
                    custom_response_dictionary['heroes'] = super_serializer.data
                elif super_type.type == "Villain":
                    custom_response_dictionary['villains'] = super_serializer.data
            return Response(custom_response_dictionary)
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
    elif request.method == "PUT":
        serializer = SuperSerializer(super, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        super.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(["PATCH"])
def supers_reassign(request, pk , power):
    super = get_object_or_404(Super, pk = pk)
    power_to_add = get_object_or_404(Power, pk = power)
    power_to_add.save()
    super.save()
    super.powers.add(power_to_add)
    serializer = SuperSerializer(super, data = request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(status = status.HTTP_200_OK)