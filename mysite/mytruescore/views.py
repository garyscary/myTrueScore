from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .leetcode import leetcode

def dashboard(request):
    test = leetcode('dt9')
    # temp = "Hello, world. You're at the polls index."
    temp = test.finishedContests()

    return render(request, 'mytruescore/dashboard.html')
