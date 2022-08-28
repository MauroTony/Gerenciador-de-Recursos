from django.urls import path
from .views import RegistrationUserView, RegistrationSuperUserView, LoginView, LogoutView,ChangePasswordView
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('register', RegistrationUserView.as_view(), name='register'),
    path('register_admin', RegistrationSuperUserView.as_view(), name='register_admin'),
    path('login', LoginView.as_view(), name='register'),
    path('logout', LogoutView.as_view(), name='register'),
    path('change-password', ChangePasswordView.as_view(), name='register'),
    path('token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
