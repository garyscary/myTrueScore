from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .leetcode import leetcode

def dashboard(request):
    test = leetcode('dt9')
    temp = test.finishedContests()
    return render(request, 'dashboard.html')
