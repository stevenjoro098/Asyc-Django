from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

@login_required
def chat_room(request):
    return render(request, 'chatroom/chat_room.html')


class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
