from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import PageSerializer
from Rag.models import Page , Question_and_Answer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated , IsAdminUser

@api_view(['GET'])
def getRoutes(request):
    
    routes = [
        {'GET': 'api/chatbot'},
        {'GET': 'api/chatbot/id'},
        # {'POST': 'api/chatbot_page/id'},

        {'POST': 'api/users/token'},
        {'POST': 'api/users/token/refresh'},
    ]

    return Response(routes)

@api_view(['GET']) # ['GET'] if some bode request Post method its not gona alow 
@permission_classes([IsAuthenticated])
def getPages(request):
    pages = Page.objects.all() # all chatbot pages
    # pages = Page.objects.filter(user_profile=request.user) # user chatbot pages
    serializer = PageSerializer(pages , many = True) # this is a class

    return Response(serializer.data)

@api_view(['GET']) 
@permission_classes([IsAuthenticated])
def getPage(request , id):
    # pages = Page.objects.all()
    page = Page.objects.get(id = id)
    serializer = PageSerializer(page , many = False) # this is a class

    return Response(serializer.data)

@api_view(['POST']) 
@permission_classes([IsAuthenticated])
def questionPage(request , id): # it send Q and A for this api and save into DB
    page = Page.objects.get(id = id)
    user = request.user 
    profile = request.user.profile
    data = request.data 

    QandA , created = Question_and_Answer.objects.get_or_create(
        page = page,
        message = data['message'],
        response = data['response'],
    )

    print('data' , data)
    serializer =  PageSerializer(page , many = False)
    return Response(serializer.data) 