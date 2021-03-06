from django.shortcuts import render
from my_app.common.LexinSport import LexinSport
from my_app.common.XiaomiSport import XiaomiSport
import json
# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request,'./templates/index.html')

def changestep(request):
    if request.method == 'GET':
        username=request.GET['username']
        password=request.GET['password']
        step=request.GET['step']
        if username in [None,'']  and password in [None,''] and step in [None,'']:
            res="请输入正确的参数"
            return render(request,'./templates/index.html',{'List': json.dumps(res)})
        res=XiaomiSport(phone=username,password=password,step=step).one_click_change_step()
        print(res)
        return render(request,'./templates/index.html',{'List': json.dumps(res)})