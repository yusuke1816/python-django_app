from django.shortcuts import render
from django.shortcuts import redirect
from .models import Friend

# from .forms import HelloForm  #この文を削除する
from .forms import FriendForm  #この文を新たに追記


from django.views.generic import ListView
from django.views.generic import DetailView


from .forms import FindForm  #この文を追記

def find(request):
  if (request.method == 'POST'):
    form = FindForm(request.POST)
    find = request.POST['find']
    data = Friend.objects.filter(name=find)
    msg = 'Result: ' + str(data.count())
  else:
    msg = 'search words...'
    form = FindForm()
    data =Friend.objects.all()
  params = {
    'title': 'Hello',
    'message': msg,
    'form':form,
    'data':data,
  }
  return render(request, 'hello/find.html', params)


class FriendList(ListView):
  model = Friend

class FriendDetail(DetailView):
  model = Friend
  
  
def index(request):
  data = Friend.objects.all()
  params = {
    'title': 'Hello',
    'data': data,
  }
  return render(request, 'hello/index.html', params)


def create(request):
  if (request.method == 'POST'):
    obj = Friend()
    friend = FriendForm(request.POST, instance=obj)
    friend.save()
    return redirect(to='/hello')
  params = {
    'title': 'Hello',
    'form': FriendForm(),
  }
  return render(request, 'hello/create.html', params)


def edit(request, num):
  obj = Friend.objects.get(id=num)
  if (request.method == 'POST'):
    friend = FriendForm(request.POST, instance=obj)
    friend.save()
    return redirect(to='/hello')
  params = {
    'title': 'Hello',
    'id':num,
    'form': FriendForm(instance=obj),
  }
  return render(request, 'hello/edit.html', params)


def delete(request, num):
  friend = Friend.objects.get(id=num)
  if (request.method == 'POST'):
    friend.delete()
    return redirect(to='/hello')
  params = {
    'title': 'Hello',
    'id':num,
    'obj': friend,
  }
  return render(request, 'hello/delete.html', params)

