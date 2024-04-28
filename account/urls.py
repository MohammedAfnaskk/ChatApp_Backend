
from django.urls import path
from . import views
from rest_framework_simplejwt.views import ( TokenObtainPairView,TokenRefreshView)
from .views import *

urlpatterns = [
    path('token/',  TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', CreateUser.as_view(), name='token_verify'),  
    path('googleregister/', GoogleRegistration.as_view(), name='Googeregister'),
    path('authuser/<int:id>', AuthUser.as_view(), name='AuthUser'),
    path('userdetails/<int:id>', UserDetils.as_view(), name='UserDetils'),
    path('logout/',LogoutView.as_view(),name='Logout')
] 