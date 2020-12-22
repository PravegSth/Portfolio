from django.shortcuts import render

def home(request):
    return render(request, 'myInfo/index.html')

def about(request):
    return render(request, 'myInfo/BackupIndex.html')

def fuu(request):
    return render(request, 'myInfo/fuu.html')


def game(request):
    return render(request, 'myInfo/test.html')