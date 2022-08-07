from django.contrib.auth.models import User

from .serializers import UserSerializer

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.authtoken.models import Token

@csrf_exempt
@api_view(['POST'])
@permission_classes([])
def login(request):
    data = JSONParser().parse(request)

    for user in User.objects.all():
        if not user:
            break
        else:
            try:
                Token.objects.get(user_id=user.id)
            except Token.DoesNotExist:
                Token.objects.create(user=user)

    try:
        user = User.objects.get(username=data["username"])
    except User.DoesNotExist:
        return JsonResponse({
            "error": "User Not Exist."
        }, status=404)

    if not user.check_password(data["password"]):
        return JsonResponse({
            "error": "Password Incorrect."
        }, status=404)

    token = Token.objects.get(user_id=user.id)
    return JsonResponse({
        "user": {
            "id": user.id,
            "username": user.username,            
        },
        "token": token.key,
    }, status=200)


@csrf_exempt
@api_view(['POST'])
@permission_classes([])
def signup(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        token = Token.objects.create(user=user)

        return JsonResponse({
            "user": serializer.data,
            "status": {
                "message": "User created.",
                "code": f"{status.HTTP_200_OK} OK",
            },
            "token": token.key,
        })

    return JsonResponse({
        "error": serializer.errors,
    }, status=400)