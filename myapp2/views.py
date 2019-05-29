from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from myapp.models import TodoItem
from datetime import datetime
import json
from django.core import serializers

#接下来要做的事情
@require_http_methods(["POST"])
def add_todo_item(request):
    response={}
    try:
        received_data = json.loads(request.body.decode('utf-8'))
        #print(received_data)

        todo_item = received_data['todo_item']
        new_date = received_data['todo_date'][0:10]
        print("step2--"+new_date)
        todo_date_time = datetime.strptime(new_date, "%Y-%m-%d")
        todo_date = datetime.date(todo_date_time)
        bFinish = received_data['bFinish']

        todo = TodoItem(todo_item=todo_item, todo_date=todo_date, bFinish=bFinish)
        #print("step3")
        todo.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except:
        response['msg'] = 'fail'
        response['error_num'] = 1
    finally:
        print("The end!")
    return JsonResponse(response)

#接下来要做的事情
@require_http_methods(["POST"])
def add_todo_items(request):
    print("add_todo_items0")
    response={}
    try:
        received_data = json.loads(request.body.decode('utf-8'))
        print("add_todo_items1")
        todo_lists= received_data['todo_lists']
        print("step1")
        ##循环进行遍历
        for todo_list in todo_lists:
            print(todo_list)
            todo_item = todo_list['todo_item']
            todo_date_time = datetime.strptime(todo_list['todo_date'], "%Y-%m-%d")
            todo_date = datetime.date(todo_date_time)
            bFinish = todo_list['bFinish']
            todo = TodoItem(todo_item=todo_item, todo_date=todo_date, bFinish=bFinish)
            todo.save()

        response['msg'] = 'success'
        response['error_num'] = 0
    except:
        response['msg'] = 'fail'
        response['error_num'] = 1
    finally:
        print("The end!")
    return JsonResponse(response)

@require_http_methods(["GET"])
def get_todo_items(request):
    response = {}
    try:
        items = TodoItem.objects.filter()

        items_list=[]
        #print("step0")
        for item in items:
            todo={}
            todo['pk'] = item.pk
            todo['todo_item'] = item.todo_item
            todo['todo_date'] = str(item.todo_date)
            todo['bFinish'] = item.bFinish
            items_list.append(todo)
        #print("step1")
        ##response['todo_lists']=json.loads(serializers.serialize("json",items_list))
        response['todo_lists'] = items_list
        #print("step3")
        response['msg'] = 'success'
        response['error_num'] = 0
    except:
        response['msg'] = 'error'
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["DELETE"])
def delete_todo_item(request):
    pass

@require_http_methods(["PUT"])
def put_todo_item(request):
    response = {}
    try:
        received_data = json.loads(request.body.decode('utf-8'))
        # print(received_data)

        #处理接收到到数据
        ##目前设置只能改变相应的事件是否能改变的状态
        id = received_data['pk']
        bFinish = received_data['bFinish']

        #修改数据
        item = TodoItem.objects.get(id=id)
        item.bFinish = bFinish
        item.save()

        response['msg'] = 'success'
        response['error_num'] = 0
    except:
        response['msg'] = 'fail'
        response['error_num'] = 1
    finally:
        print("The end!")
    return JsonResponse(response)