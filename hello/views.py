from django.shortcuts import render

def index(request):
  params = {
    'title':'Hello/Index',
    'msg':'お名前は？',
  }
  return render(request, 'hello/index.html', params)

def form(request):
  msg = request.POST['msg']
  params = {
    'title':'Hello/Form',
    'msg':'こんにちは、' + msg + 'さん。',
  }
  return render(request, 'hello/index.html', params)
