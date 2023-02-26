# from django.http import HttpResponse
from django.shortcuts import render

def index(req):
	params = {'name':'Harsh','city':'Surat',"email":'patelharsh9797@gmail.com'};
   	# return HttpResponse("<h1>Harsh<h1>");
	return render(req,'index.html',params);