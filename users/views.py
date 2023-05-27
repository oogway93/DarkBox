from django.shortcuts import render


def lol(request):
    return render(request, 'users/lol.html')
