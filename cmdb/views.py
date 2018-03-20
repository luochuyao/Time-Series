# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response, render
# import ClassficationModel
# from ClassficationModel import *
# Create your views here.
from django.shortcuts import HttpResponse
from django.template import loader
import numpy as np
import matplotlib.pyplot as plt
import os
from cmdb import models, ClassificationModel
# from cmdb import tests


def index_1(request):
    return render(request, 'index.html',)


def receive_data(request):

    if request.GET:
        print('submitted')
        method = request.GET.get('method')
        file = request.GET.get('file')
        result = ClassificationModel.execute_data(file, method)
        table_content = [[result[0], result[1], result[2]]]
        return render(request, 'result.html', {'table': table_content})

    return render(request, 'signalpointdata.html', locals())
