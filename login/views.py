# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        sname = request.POST.get('userNum')
        pwd = request.POST.get('userPw')

        try:
            if sname == 'admin' and pwd == 'admin123':
                return render(request, 'index.html')
        except:
            return HttpResponse('denglushibai')

