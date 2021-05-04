# -*- coding:utf-8 -*-
# @Time   :2021/5/4 18:15
# @Author :CharlesYim
# @File   :forms.py
from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        error_messages = {
            'thumbnail': {
                'invalid_image': '请上传正确格式的图片！'
            }
        }
