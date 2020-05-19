from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from .models import TodoList, Comment
from users.models import CustomUser
from django.urls import reverse_lazy

class AuthorProfileView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'users/author_profile.html'
    login_url = 'login'
    context_object_name = 'userlist'

    def get_queryset(self):
        username = get_object_or_404(CustomUser, pk = self.kwargs['pk'])
    
        return CustomUser.objects.filter(username=username)

    def get_context_data(self, *args, **kwargs):
        model = TodoList
        context = super(AuthorProfileView, self).get_context_data(*args, **kwargs)
        context['todolist'] = TodoList.objects.filter(autore= self.kwargs['pk']).order_by('-creato')[:10]
        return context

class TodoListView(LoginRequiredMixin, ListView):
    model = TodoList
    template_name = 'todo/todo_list.html'
    login_url = 'login'
    context_object_name = 'todolist'
    
    def get_queryset(self):
        autore = self.request.user
    
        return TodoList.objects.filter(autore=autore).order_by('-creato')
    

class TodoDetailView(LoginRequiredMixin, DetailView):
    model = TodoList
    template_name = 'todo/todo_dettaglio.html'
    login_url = 'login'


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = TodoList
    template_name = 'todo/todo_nuovo.html'
    fields = ('titolo', 'contenuto', 'scade_il', 'tag', 'orario', 'pubblica')
    success_url = reverse_lazy('todo_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.autore = self.request.user
        return super().form_valid(form)


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = TodoList
    template_name = 'todo/todo_edit.html'
    fields = ['titolo', 'contenuto', 'scade_il', 'tag', 'orario', 'pubblica']
    success_url = reverse_lazy('todo_list')
    login_url = 'login'


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = TodoList
    template_name = 'todo/todo_elimina.html'
    success_url = reverse_lazy('todo_list')
    login_url = 'login'

class SocialListView(LoginRequiredMixin, ListView):
    model = TodoList
    template_name = 'social_list.html'
    login_url = 'login'
    context_object_name = 'sociallist'
    
    def get_queryset(self):
        autore = self.request.user
        return TodoList.objects.filter(pubblica="Pubblica").exclude(autore=autore).order_by('-creato')

class CommentListView(LoginRequiredMixin, ListView):
    model = Comment
    template_name = 'comment/comment_list.html'
    login_url = 'login'
    context_object_name = 'commentlist'
        
    def get_context_data(self, *args, **kwargs):
        model = TodoList
        context = super(CommentListView, self).get_context_data(*args, **kwargs)
        context['todolist'] = TodoList.objects.filter(autore_id= self.kwargs['pk']).order_by('-creato')[:10]
        return context

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comment/comment_nuovo.html'
    fields = ('testo',)
    success_url = reverse_lazy('social_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.autore = self.request.user
        form.instance.todo = get_object_or_404(TodoList, pk = self.kwargs['pk'])
        return super().form_valid(form)


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    template_name = 'comment/comment_edit.html'
    fields = ['testo',]
    success_url = reverse_lazy('social_list')
    login_url = 'login'


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comment/comment_elimina.html'
    success_url = reverse_lazy('social_list')
    login_url = 'login'
