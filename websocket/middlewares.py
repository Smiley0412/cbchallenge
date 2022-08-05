from urllib.parse import parse_qs

from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from rest_framework.authtoken.models import Token

User = get_user_model()


@database_sync_to_async
def get_user(token):
    try:
        access_token = Token.objects.get(key=token)
        try:
            return User.objects.get(id=access_token.user_id)
        except User.DoesNotExist:
            return AnonymousUser()
    except Token.DoesNotExist:
        return AnonymousUser()


class WebSocketJWTAuthMiddleware:

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        parsed_query_string = parse_qs(scope["query_string"])
        token = parsed_query_string.get(b"token")[0].decode("utf-8")

        scope["user"] = await get_user(token)

        return await self.app(scope, receive, send)
