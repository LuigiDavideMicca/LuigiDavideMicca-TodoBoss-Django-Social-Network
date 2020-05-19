from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from todo_platform.models import TodoList

class UserPageView(LoginRequiredMixin, generic.ListView):
    model = TodoList
    template_name = 'users/user_page.html'
    login_url = 'login'
    context_object_name = 'todolist'
    
    def get_queryset(self):
        autore = self.request.user
    
        return TodoList.objects.filter(autore=autore)[:4]

class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

class UserChangeView(LoginRequiredMixin, generic.UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('user_page')
    template_name = 'users/user_change.html'
    login_url = 'login'