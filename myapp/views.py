from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
from .models import TodoItem
from datetime import date
import requests
import json

#接下来要做的事情
@require_http_methods(["GET"])
def add_todo_item(request):
    response={}
    try:
        todo_item = request.GET.get("todo_item")
        year = int(request.GET.get('year'))
        month = int(request.GET.get('month'))
        day = int(request.GET.get('day'))

        todo_date = date(year,month,day)

        bFinish = request.GET.get("bfinish") ##大小写非常敏感

        todo=TodoItem(todo_item=todo_item,todo_date=todo_date,bFinish=bFinish)
        todo.save()

        print("the end")

        response['msg']='success'
        response['error_num']=0
    except:
        response['msg'] = 'error'
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def get_todo_item(request):
    response = {}
    try:
        items = TodoItem.objects.filter()
        response['list']=json.loads(serializers.serialize("json",items))
        response['msg'] = 'success'
        response['error_num'] = 0
    except:
        response['msg'] = 'error'
        response['error_num'] = 1

    return JsonResponse(response)