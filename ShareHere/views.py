from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def subject1(request):
    return render(request, 'subject1.html')

def subject2(request):
    return render(request, 'subject2.html')

def subject3(request):
    return render(request, 'subject3.html')

def subject4(request):
    return render(request, 'subject4.html')

def subject5(request):
    return render(request, 'subject5.html')

def subject6(request):
    return render(request, 'subject6.html')
