from django.shortcuts import render,redirect
from .forms import MusicianForm

# Create your views here.
def add_musician(request):
    if request.method == 'POST':
        add_musician = MusicianForm(request.POST)
        if add_musician.is_valid():
            add_musician.save()
            return redirect('add_musician')
    else:
       add_musician = MusicianForm() 
    return render(request, 'musician/add_musician.html',{'form':add_musician})