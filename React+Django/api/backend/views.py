from urllib import response
from django.shortcuts import render
from backend.models import Todo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from backend.serializers import TodoSerializer
# Create your views here.

@api_view(['GET'])
def apiCall(request):
    api_urls = {
        'todos':"/todos/",
        'todos add':"/todosadd/",
        'todos update':"/todosupdate/<int:id>/",
        'todos delete':"/todosdelete/<int:id>/",
        'todoscompleted':"/todoscompleted/<int:id>/",
    }
    return Response(api_urls)


@api_view(['GET'])
def todos(request):
    todoslist = Todo.objects.all()
    serializers = TodoSerializer(todoslist, many=True)
    return Response(serializers.data)