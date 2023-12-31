from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from .models import User, Follow
from .serializers import UserSerializer


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
def check_user(request):
    username = request.GET['username']

    if User.objects.filter(username=username).exists():
        return Response(status=200)
    return Response(status=400)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_me(request):
    serializer = UserSerializer(request.user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_user(request):
    pk = request.GET.get('user-id')

    user = User.objects.get(pk=pk)

    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def follow(request, *args, **kwargs):

    try:
        user_id = request.data.get('user-id')
        user = User.objects.get(id=user_id)

        follow = Follow.objects.filter(follow=request.user, user=user)

        if follow.exists():
            follow[0].delete()

        else:
            follow = Follow.objects.create(
                user=user,
                follow=request.user,
            )

        return Response(status=200)

    except Exception as e:
        print(e)

        return Response({'error': str(e).strip()}, status=404)
