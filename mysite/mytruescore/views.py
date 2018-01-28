from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .scraper import *

def dashboard(request):
    test = leetcode('dt9').solvedQuestions()
    test = firecode('12834').solvedQuestions()
    # return HttpResponse(test)
    return render(request, 'dashboard.html')