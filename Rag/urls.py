from django.urls import path
from . import views


urlpatterns = [
    path('' ,views.homepage ,name = 'home_page'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('chatbot/<uuid:id>/', views.page_detail, name='chatbot_page'),
    # path('get_chatbot_response/', views.get_chatbot_response, name='get_chatbot_response'),

]

  