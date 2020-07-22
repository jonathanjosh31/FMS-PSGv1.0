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

class StudentList(APIView):
    permission_classes = [IsAdminUser]

    def get(self,request):

        model = StudentAccount.objects.all()
        serializer = StudentSerializer(model,many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = StudentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#unique id required for student detail to work (Creation Needed)

class StudentDetail(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request,name):
        try:
            model = StudentAccount.objects.get(username = name)
        except StudentAccount.DoesNotExist:
            return Response('Student not found', status= status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(model)
        return Response(serializer.data)

    def put(self,request,name):
        try:
            model = StudentAccount.objects.get(username = name)
        except StudentAccount.DoesNotExist:
            return Response('Student not found', status= status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(model,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class VisitorList(APIView):
    permission_classes = [IsAdminUser]

    def get(self,request):

        model = Visitor.objects.all()
        serializer = VisitorSerializer(model,many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = VisitorSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class VisitorDetail(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request,time):
        try:
            model = Visitor.objects.get(timestamp = time)
        except Visitor.DoesNotExist:
            return Response('Visitor not found', status= status.HTTP_404_NOT_FOUND)
        serializer = VisitorSerializer(model)
        return Response(serializer.data)

    def put(self,request,time):
        try:
            model = Visitor.objects.get(timestamp = time)
        except Visitor.DoesNotExist:
            return Response('Visitor not found', status= status.HTTP_404_NOT_FOUND)

        serializer = VisitorSerializer(model,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
