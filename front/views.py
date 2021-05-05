from django.shortcuts import render
from django.views import View
from .models import Image
from django.http import HttpResponse,FileResponse
from django.utils.http import urlquote
from .forms import ImageForm
import json
import time
import os


class IndexView(View):
    def get(self,request):
        return render(request,'index.html')

    def post(self,request):
        pass
        return HttpResponse('wait……')


def upload(request):
    '''
    上传图片接口
    :param request:
    :return:
    '''
    if request.method == 'POST':
        thumbnail = request.FILES.get('file')
        with open(os.path.join('media',str(thumbnail)), 'wb') as fp:
            for chunk in thumbnail.chunks():
                fp.write(chunk)

        context = {
            "code": 200,
            "message": "success",
            "data": {
                "name": thumbnail.name
            }
        }
        time.sleep(1)
        return HttpResponse(json.dumps(context), content_type="application/json")



def modify(request):
    '''
    修改图片接口：包括尺寸颜色
    前端传来的是两个参数：name图片的名称在服务器用os.path.join('media',name)可以读取本地服务器图片
    另一个参数是size或color
    读取本地图片后 与size或color一起传入修改图片函数，函数返回图片保存到本地，再返回前端本地图片名称file
    :param request:
    :return:
    '''
    if request.method == 'POST':
        name = request.POST.get('name')
        size = request.POST.get('size')

        time.sleep(1)
        #bbs.PNG替换修改生成后图片的名称
        return HttpResponse(json.dumps({'name':'bbs.PNG'}), content_type="application/json")


def download(request,name):
    '''
    下载图片接口
    :param request:
    :param name:
    :return:
    '''
    try:
        with open(os.path.join('media',name),'rb') as fp:
            response = HttpResponse(fp.read())
            response['Content-Type'] = "application/octet-stream"
            response['Content-Disposition'] = f'attachment;filename={name}'
        return response
    except Exception:
        return HttpResponse('没有可下载图片')
