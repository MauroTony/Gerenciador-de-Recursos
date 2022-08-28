from rest_framework.response import Response
from rest_framework.views import APIView, status


class HelloWorldAPIView(APIView):
    def get(self, request):
        return Response({'message': 'Hello World!'}, status=status.HTTP_200_OK)
