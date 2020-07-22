from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS

from rest_framework.authtoken.models import Token

from rest_framework.views import APIView

from rest_framework.generics import RetrieveAPIView

from rest_framework.response import Response

from rest_framework import status

from .serializers import *

class UserAuthentication(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(data = request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token , created = Token.objects.get_or_create(user=user)
        return Response(token.key)


class DeviceList(APIView):
    permission_classes = [IsAdminUser]

    def get(self,request):

        model = Device.objects.all()
        serializer = DeviceSerializer(model,many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = DeviceSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class DeviceDetail(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self,request,name):
        try:
            model = Device.objects.get(device = name)
        except Device.DoesNotExist:
            return Response('Device not found', status= status.HTTP_404_NOT_FOUND)
        serializer = DeviceSerializer(model)
        return Response(serializer.data)

    def put(self,request,name):
        try:
            model = Device.objects.get(device = name)
        except Device.DoesNotExist:
            return Response('Device not found', status= status.HTTP_404_NOT_FOUND)

        serializer = DeviceSerializer(model,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)