from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homeFun(request):
    # return HttpResponse("Hello World again!")
    # return render(request, 'home.html')   # Returns static html
    return render(request, 'home.html', {'greetName':'Varun'})  # Return dynamic content in html

def okFun(request):
    # return HttpResponse("OK OK OK")
    return render(request, 'ok.html')

def addUsingGetFun(request):
    num1 = int(request.GET['num1'])
    num2 = int(request.GET['num2'])
    return render(request, 'result.html', {'sum': num1 + num2})

def addUsingPostFun(request):
    num1 = int(request.POST['numPost1'])
    num2 = int(request.POST['numPost2'])
    return render(request, 'result.html', {'sum': num1 + num2})