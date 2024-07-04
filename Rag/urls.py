from django.urls import path
from . import views


urlpatterns = [
    path('' ,views.homepage ,name = 'home_page'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('chatbot/<uuid:id>/', views.page_detail, name='chatbot_page'),

    path('article_list/', views.article_list, name='article_list'),
    path('article/<int:id>/', views.article_detail, name='article_detail'),
    path('article/new/', views.article_create, name='article_create'),
    path('article/<int:id>/edit/', views.article_edit, name='article_edit'),
    path('article/<int:id>/delete/', views.article_delete, name='article_delete'),
]

