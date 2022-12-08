from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import Chattapp.routing

application = ProtocolTypeRouter({  # automatically maps HTTP request to the standard django views if no specific http
    # mapping is provided
    'websocket': AuthMiddlewareStack(
        URLRouter(  # is used to map websocket connections to the URLs defined in websocket_urlpatterns.
            Chattapp.routing.websocket_urlpatterns
        )
    ),
})
