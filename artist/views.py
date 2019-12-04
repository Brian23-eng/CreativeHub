from django.shortcuts import render, redirect


def home(request):
    title = 'Creative || Hub'
    
    return render(request, 'index.html',{'title': title})


