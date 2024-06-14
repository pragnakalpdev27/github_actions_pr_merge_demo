from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, GitHub Actions!")

def demo(request):
    return HttpResponse("Hello, GitHub Actions demo!")
