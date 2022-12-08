from django.urls import re_path
from . import consumers

# mapping the url patterns to the consumers.
# re_path is used to define url with regular expression.
websocket_urlpatterns = [
    re_path(r'ws/chat/', consumers.ChatConsumer),
]