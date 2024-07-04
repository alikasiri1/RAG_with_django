from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import PageSerializer
from Rag.models import Page


@api_view(['GET'])
def getRoutes(request):
    
    routes = [
        {'GET': 'api/chatbot'},
        {'GET': 'api/chatbot/id'},
        {'POST': 'api/users/token'},
        {'POST': 'api/users/token/refresh'},
    ]

    return Response(routes)

@api_view(['GET']) # ['GET'] if some bode request Post method its not gona alow 
def getPages(request):
    pages = Page.objects.all() # all chatbot pages
    # pages = Page.objects.filter(user_profile=request.user) # user chatbot pages
    serializer = PageSerializer(pages , many = True) # this is a class

    return Response(serializer.data)

@api_view(['GET']) 
def getPage(request , id):
    # pages = Page.objects.all()
    page = Page.objects.get(id = id)
    serializer = PageSerializer(page , many = False) # this is a class

    return Response(serializer.data)
