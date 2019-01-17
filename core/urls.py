from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'userlist/', views.UserList, name='user_list'),
    url(r'generate/',views.GenerateRandomUserView.as_view(),name='generate'),
]