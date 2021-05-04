from django.shortcuts import render
from django.views import View
from .models import Image
from django.http import HttpResponse
from .forms import ImageForm
import json
import time


class IndexView(View):
    def get(self,request):
        return render(request,'index.html')

    def post(self,request):
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            thumbnail = form.cleaned_data['thumbnail']
            print(thumbnail)
            context = {
                'thumbnail':thumbnail
            }
            return render(request,'index.html',context=context)
        else:
            print(form.errors.get_json_data())
            return HttpResponse('fail')


def modify(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        size = request.POST.get('size')
        print(size)
        time.sleep(1)
        return HttpResponse(json.dumps({'name':'bbs.PNG'}), content_type="application/json")