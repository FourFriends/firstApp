from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'add_todo_item$', views.add_todo_item,),
    url(r'get_todo_item$', views.get_todo_item,),

]