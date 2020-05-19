from django.urls import path
from django.conf.urls import url
from .views import (
    TodoListView, 
    TodoDetailView, 
    TodoCreateView, 
    TodoUpdateView,
    TodoDeleteView,
    SocialListView,
    CommentListView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    AuthorProfileView,
    )

urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('todo/<int:pk>', TodoDetailView.as_view(), name='todo_dettaglio'),
    path('todo/nuovo', TodoCreateView.as_view(), name='todo_nuovo'),
    path('todo/<int:pk>/modifica', TodoUpdateView.as_view(), name='todo_edit'),
    path('todo/<int:pk>/elimina', TodoDeleteView.as_view(), name='todo_elimina'),
    path('comments/<int:pk>', CommentListView.as_view(), name='comment_list'),
    path('comment/nuovo/<int:pk>', CommentCreateView.as_view(), name='comment_nuovo'),
    path('comment/<int:pk>/modifica', CommentUpdateView.as_view(), name='commento_edit'),
    path('comment/<int:pk>/elimina', CommentDeleteView.as_view(), name='comment_elimina'),
    path('social/', SocialListView.as_view(), name='social_list'),
    path('social/user/<int:pk>/', AuthorProfileView.as_view(), name='author_profile'),
]