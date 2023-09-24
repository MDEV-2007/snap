from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework import status,viewsets

from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from .models import User
from .serializers import UserSerializer


from django.http.response import JsonResponse
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import JSONParser
from .models import Follow
from .serializers import FollowSerializer




### Check User


# @api_view(['GET'])
# def check_user(request):
#     serializer = UserSerializer(request.user)
#     return Response(serializer.data)


@api_view(['GET'])
def check_user(request):
    username = request.GET['username']

    if User.objects.filter(username=username).exists():
      return Response(status=200)
    return Response(status=400)


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():

        user = serializer.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})

    return Response(serializer.errors, status=status.HTTP_200_OK)


@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data})


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed!")


    

class FollowViewSet(viewsets.ModelViewSet):

    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        data = request.data
        data['account'] = request.user.id
        serialzier = serialzier_class(data= data)
        if serialzier.is_valid():
            serialzier.save()
            return JsonResponse(serialzier.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serialzier.errors, status=status.status.HTTP_405_METHOD_NOT_ALLOWED)
