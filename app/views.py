from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'name':'harini','age':111,'score':99,'income':50000}
    return render(request,'condition.html',context=d)