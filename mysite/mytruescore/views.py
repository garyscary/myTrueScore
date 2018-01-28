from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .scraper import *

def dashboard(request):

    uvaScore = uva("tianzhi")
    # leetCodeScore = leetcode('dt9').solvedQuestions()
    # firecodeScore = firecode('12834').solvedQuestions()
    leetcodeScore = leetcode("tianzhi").solvedQuestions()
    firecodeScore = firecode("12824")
    totalProblemsSolved  = uvaScore + firecodeScore
    return render(request, 'dashboard.html',{'problemsSolved': totalProblemsSolved})
    
    