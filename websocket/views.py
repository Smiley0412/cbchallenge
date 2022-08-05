from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Messages
from .serializers import MessageSerializer

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth import get_user_model

User = get_user_model()

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_list(request):
    users = User.objects.values('id', 'username')
    return JsonResponse(list(users), safe=False)

"""
List of messages, or Create message
Allow if not exist csrf token
Only Allow GET and POST method
"""
@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def messages_list(request):
    channel_layer = get_channel_layer()

    if request.method == "GET":
        params = request.query_params
        if params.get('sent'):
            """
            List of messages sent by user
            """
            messages = Messages.objects.filter(by=params.get('user')).all()
            serializer = MessageSerializer(messages, many=True)
            return JsonResponse(serializer.data, safe=False)

        else:
            """
            List of messages sent by user
            """
            messages = Messages.objects.filter(to=params.get('user')).all()
            serializer = MessageSerializer(messages, many=True)
            return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        """
        Create Message
        """
        data = JSONParser().parse(request)        
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            socket_message = f"{serializer.data['sent_from']} sent message {serializer.data['id']}"
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                f"{serializer.data['to']}-message", 
                { "type": "send_last_message", "text": socket_message, "id": serializer.data['id'] }
            )
            return JsonResponse(serializer.data, status=201)
        return JsonResponse({
            "error": serializer.errors,
        }, status=400)


"""
Show single message
Allow if not exist csrf token
Only Allow GET and DELETE method
"""
@csrf_exempt
@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def message_detail(request, pk):
    """
    Get single message by primary key.
    If not exist, return not exist response.
    """
    try:
        message = Messages.objects.get(pk=pk)
    except Messages.DoesNotExist:
        return JsonResponse({
            "error": "Message is not exist!"
        }, status=404)

    if request.method == "GET":
        """
        Return single message
        """
        serializer = MessageSerializer(message)
        return JsonResponse(serializer.data)
    
    elif request.method == "DELETE":
        """
        Delete single message
        """
        message.delete()
        return JsonResponse({}, status=204)