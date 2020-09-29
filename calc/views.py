from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return render(request,'home.html',{'name':'jaya'})

import re
def add(request):
  str_1 = request.GET["num1"]
  str_2 = request.GET["num2"]
  
  
  regular_ex = re.compile(str_1)
  match_input = regular_ex.match(str_2)
  try:
    answer = match_input.group()
  except AttributeError:
    answer=None
  if (answer == str_2):
      result="YES"
  else:
      result="NO"
  return render(request,'home.html',{'result':result})