from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'add_todo_item$', views.add_todo_items,),
    url(r'get_todo_item$', views.get_todo_items,),
    url(r'sum$',views.get_sum,),

]