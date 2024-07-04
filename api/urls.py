from django.urls import path
from . import views


urlpatterns = [
    path('' ,views.getRoutes),
    path('chatbot/' ,views.getPages),
    path('chatbot/<uuid:id>/' ,views.getPage),
    ]