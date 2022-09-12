from django.shortcuts import render,redirect
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def create(requrest):
    if requrest.method == 'POST':
        url = requrest.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link = url,uuid = uid)
        new_url.save()
        return HttpResponse(uid)

def go (request, pk):
    url_detail = Url.objects.get(uuid=pk)
    return redirect(url_detail.link)
    