from django.http      import HttpResponse
from django.shortcuts import render, redirect

from .forms  import TextBlobForm
from .models import TextBlob

# display the inut form and save the input
# add count of the text blobs in the database
def index(req):
    count_blobs =  TextBlob.objects.count()
    if req.method == "POST":
        form = TextBlobForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = TextBlobForm()
    return render(req, 'index.html', {'form': form, 'count_blobs': count_blobs})

# display success and count of text blobs
def success(req):
    count_blobs =  TextBlob.objects.count()
    return render(req, 'success.html', {'count_blobs': count_blobs})
