from django.urls import path
from .views import RegistrationUserView, RegistrationSuperUserView, LoginView, LogoutView,ChangePasswordView, DeleteUserView, ResourcesListView, ResourceView, ResourceScheduleView
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('register', RegistrationUserView.as_view(), name='register'),
    path('register_admin', RegistrationSuperUserView.as_view(), name='register_admin'),
    path('delete_user', DeleteUserView.as_view(), name='delete_user'),
    path('login', LoginView.as_view(), name='register'),
    path('logout', LogoutView.as_view(), name='register'),
    path('change_password', ChangePasswordView.as_view(), name='register'),
    path('token_refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('list_resources', ResourcesListView.as_view(), name='resources'),
    path('resource', ResourceView.as_view(), name='resources'),
    path('resource_schedule', ResourceScheduleView.as_view(), name='resources_schedule'),
]
