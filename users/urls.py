from django.urls import path
from django.conf.urls import url
from .views import UserPageView, SignupPageView, UserChangeView

urlpatterns = [
    path('', UserPageView.as_view(), name='user_page'),
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('modifica-account/<int:pk>', UserChangeView.as_view(), name='user_change'),
]