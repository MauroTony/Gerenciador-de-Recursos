from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from  rest_framework.generics import ListAPIView
from ..utils import get_tokens_for_user
from ..models import Resources, ResourceScheduling
from ..serializers import RegistrationSerializer, PasswordChangeSerializer, ResourcesSerializer, ResourceSchedulingSerializer

class ResourcesListView(ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = ResourcesSerializer
    queryset = Resources.objects.all()


class ResourceView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request):
        serializer = ResourcesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.create()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        data = request.data
        if "id" not in data or "description" not in data or "available" not in data:
            return Response({'msg': 'missing data'},
                            status=status.HTTP_400_BAD_REQUEST)
        resource_id = data["id"]
        try:
            resource = Resources.objects.get(id=resource_id)
            serializer = ResourcesSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.update(resource)
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        except Resources.DoesNotExist:
            return Response({'msg': 'Resource not found'},
                            status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        data = request.data
        if "id" not in data:
            return Response({'msg': 'missing data'},
                            status=status.HTTP_400_BAD_REQUEST)
        resource_id = data["id"]
        try:
            resource = Resources.objects.get(id=resource_id)
            resource.delete()
            return Response({'msg': 'Resource successfully deleted'},
                            status=status.HTTP_200_OK)
        except Resources.DoesNotExist:
            return Response({'msg': 'Resource not found'},
                            status=status.HTTP_404_NOT_FOUND)


class ResourceScheduleView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        resource = ResourceScheduling.objects.filter(is_deleted=False)
        serializer = ResourceSchedulingSerializer(resource, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        if "resource" not in data or "initial_date" not in data or "final_date" not in data:
            return Response({'msg': 'missing data'},
                            status=status.HTTP_400_BAD_REQUEST)
        resource_id = data["resource"]
        print("data: ", data)
        data_dict = { "user": request.user.id,  **data}
        print("data: ", data_dict)
        try:
            resource = Resources.objects.get(id=resource_id)
            if not resource.available:
                return Response({'msg': 'Resource unavailable'},
                                status=status.HTTP_400_BAD_REQUEST)
            print("data: ", data_dict)
            serializer = ResourceSchedulingSerializer(
                data=data_dict
            )
            serializer.is_valid(raise_exception=True)
            print("valido")
            serializer.create()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Resources.DoesNotExist:
            return Response({'msg': 'Resource not found'},
                            status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        data = request.data
        if "resource_id" not in data:
            return Response({'msg': 'missing data'},
                            status=status.HTTP_400_BAD_REQUEST)
        resource_id = data["resource_id"]
        try:
            resource = ResourceScheduling.objects.get(id=resource_id)
            serializer = ResourceSchedulingSerializer()
            serializer.delete(resource, request.user)
            return Response({'msg': 'Resource successfully deleted'},
                            status=status.HTTP_200_OK)
        except Resources.DoesNotExist:
            return Response({'msg': 'Resource not found'},
                            status=status.HTTP_404_NOT_FOUND)
