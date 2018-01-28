from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .leetcode import leetcode

def dashboard(request):
    test = leetcode('dt9').solvedQuestions()
    return render(request, 'dashboard.html')