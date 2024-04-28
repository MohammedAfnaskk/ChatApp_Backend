 # ChatApp/asgi.py

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chatserver.routing  
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChatApp.settings')
application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                chatserver.routing.websocket_urlpatterns
            )
        ),
    }
)
