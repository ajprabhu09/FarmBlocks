from django.shortcuts import render,redirect
from django.http import HttpResponse
import pybry
from .forms import UploadFileForm
import json
import requests
import os
lbry = pybry.LbryApi()
import datetime
balance_response = lbry.account_balance()
# Create your views here.
def homepage(request):
	lbry = pybry.LbryApi()
	balance_response = lbry.account_balance()
	
	# return HttpResponse('HEllo')
	print(balance_response[0])
	if balance_response[1].status_code == 200:
		return render(request,'main/index.html',context={'balance':balance_response[0]})
	else:
		return render(request,'main/index.html',context={'balance':-1})
def products(request):
	return render

def commit_to_block_chain(filename):
	print("PUBLISHING TO BLOCKCHAIN....",end='')
	# lbry.publish(channel_name="@asdasdasdasd",
	# 			 name="OrdersJson",
	# 			 bid='0.001',
	# 			 file_path=f"{filename}")
	method = '{"method":"publish","params":{"channel_name":"@asdasdasdasd","name":"DetailsJson","bid":"0.001","file_path":"/home/ajinkya/Desktop/a.jpg"}}'
	method = json.loads(method)
	method['params']['file_path']=os.path.abspath(filename)

	print(method)	
	response = requests.post('http://localhost:5279',json=method)
	print(response.text)
	print("DONE")


def upload(request):
	lbry = pybry.LbryApi()
	balance_response = lbry.account_balance()
	print("********UPLOAD")
	if request.method == 'POST':
		form = UploadFileForm(request.POST)
		print(form.is_valid())
		if form.is_valid():
			json_old = None
			with open('./upload.json') as file:
				json_old = json.load(file)

				print(json_old)
			with open('./upload.json',"w+") as file:
				# json_string = json.dumps({'time':str,'data':form.cleaned_data})

				# file.write(","+json_string)
				# print("Saved File")
				json_old.append({'time':str(datetime.datetime.now()),'data':form.cleaned_data})
				json_string = json.dumps(json_old)
				file.write(json_string)

				print(json_old)
			commit_to_block_chain('upload.json')
			return render(request,'main/index.html',context={'balance':balance_response[0]})
		else:
			form = UploadFileForm()
			return render(request,'main/index.html',context={'balance':balance_response[0]})


	else:
		form = UploadFileForm()
		return render(request,'main/upload.html',{'form':form})