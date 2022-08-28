from django.urls import path
from .views import (
    HelloWorldAPIView,
)

urlpatterns = [
    path("helloworld", HelloWorldAPIView.as_view()),
]
