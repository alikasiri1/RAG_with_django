from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('' ,views.getRoutes),
    path('chatbot/' ,views.getPages),
    path('chatbot/<uuid:id>/' ,views.getPage),
    path('chatbot_page/<uuid:id>/' ,views.questionPage),

    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]