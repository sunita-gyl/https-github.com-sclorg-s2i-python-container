from django.shortcuts import render


def home(request):
  results = {}
  return render(request,'home/index.html', results)


