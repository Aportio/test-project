from django.http      import HttpResponse
from django.shortcuts import render, redirect

from .forms  import TextBlobForm
from .models import TextBlob

def index(req):
    if req.method == "POST":
        form = TextBlobForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = TextBlobForm()
    return render(req, 'index.html', {'form': form})

def success(req):
    return render(req, 'success.html')
