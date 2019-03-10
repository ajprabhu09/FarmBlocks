from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
	# return HttpResponse('HEllo')
	return render(request,'main/index.html',context={})