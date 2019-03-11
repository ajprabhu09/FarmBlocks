from django.shortcuts import render,redirect
from django.http import HttpResponse
import pybry
from .forms import UploadFileForm

lbry = pybry.LbryApi()
balance_response = lbry.account_balance()
# Create your views here.
def homepage(request):
	
	
	# return HttpResponse('HEllo')
	print(balance_response[0])
	if balance_response[1].status_code == 200:
		return render(request,'main/index.html',context={'balance':balance_response[0]})
	else:
		return render(request,'main/index.html',context={'balance':-1})
def products(request):
	return render

def upload(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST,request.FILES)
		print(form.is_valid())
		if form.is_valid():
			print(request.FILES['file'])
			print("Recieved FIL *************************")
			return render(request,'main/index.html',context={'balance':balance_response[0]})
		else:
			form = UploadFileForm()
			return render(request,'main/index.html',context={'balance':balance_response[0]})


	else:
		form = UploadFileForm()
		return render(request,'main/upload.html',{'form':form})