# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from random import shuffle


VALUES = ['ice', 'watermelon', 'a bundle of leaves', 'torch', 'boots', 'knife', 'water', 'the ocean', 'yo momma', 'pie']



# Create your views here.
def index(request):
    if 'number' not in request.session:
        request.session['number'] = 0
    return render(request, 'surprise_app/index.html')

def process(request):
    if request.method == "POST":
        shuffle(VALUES)
        request.session['number'] = request.POST['number']
    return redirect('/results')

def results(request):
    num = int(request.session['number'])
    # context = {
    #     'number' : range(num),
    #     'values' : VALUES
    # }
    context = {
        'number' : num,
        'values' : VALUES
    }
    print context
    return render(request, 'surprise_app/results.html', context)

