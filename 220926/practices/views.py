from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def ping(request):
    return render(request, 'ping.html')

def pong(request):
    # name = request.GET.get('ball')
    # context = {
    #     'name': name,
    # }
    return render(request, 'pong.html', {
        'name': request.GET.get('ball'),
        })