from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse('This is Home Page')
    return render(request,'index.html')
def pythond(request):
    return render(request,'pythond.html')
def pythonmt(request):
    return render(request,'pythonmt.html')
def pythonat(request):
    return render(request,'pythonat.html')
def sql(request):
    return render(request,'sql.html')
def web(request):
    return render(request,'web.html')
def apti(request):
    return render(request,'apti.html')
def verbal(request):
    return render(request,'verbal.html')
def contact(request):
    return render(request,'contact.html')
def placements(request):
    return render(request,'placements.html')
def fresher(request):
    return render(request,'fresher.html')