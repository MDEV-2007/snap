from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'screen/index.html')


def explore(request):
    return render(request, 'screen/explore.html')


def search(request):
    return render(request, 'screen/search.html')


def notification(request):
    return render(request, 'screen/notification.html')


def reels(request):
    return render(request, 'screen/reels.html')

def create(request):
    return render(request, 'screen/create.html')


def message(request):
    return render(request, 'screen/message.html')


def profile(request):
    return render(request, 'screen/profile.html')