from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'post_todo_item$', views.add_todo_item,),
    url(r'add_todo_items$', views.add_todo_items,),
    url(r'get_todo_items$', views.get_todo_items),
    url(r'put_todo_item$',views.put_todo_item),
    url(r'delete_todo_item$',views.delete_todo_item),
]