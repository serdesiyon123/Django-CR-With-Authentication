from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.http import  Http404
from .forms import viewForm
from .models import DB

@login_required(login_url='/login')
def home(request):
    if request.method == 'GET':
        form = viewForm()
        return render(request, 'home.html', context={'form': form})
    else:
        form = viewForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
           form.save()
           return redirect('/list')




def list(request):
    if request.method == 'POST':

       post_id = request.POST.get('post_id')
       post = DB.objects.filter(id=post_id).first()
       if post and post.name == request.user:
          post.delete()


    li = DB.objects.all()
    return render(request,'list.html', {'li': li})


def all(request, store_id):
    store = DB.objects.get(pk=store_id)
    if store is not None:
        return render(request, 'store.html', {'store': store})
    else:
        raise Http404("Page does not exist")


