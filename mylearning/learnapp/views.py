from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProfileSerializer
from .models import ProfileModel
from rest_framework.viewsets import ViewSet


class ProfileView(ViewSet):
    def list(self, request):
        print(request.user)
        queryset = ProfileModel.objects.all().values()
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
