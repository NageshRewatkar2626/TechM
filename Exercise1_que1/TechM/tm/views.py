from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.generic import View
from tm.models import RouterModel
from django.contrib import messages 
# from django.db.utils import IntegrityError

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
class RouterDetails(View):
	def post(self,request):
		r_name	= request.POST.get('e1')

		RouterModel(router_name=r_name).save()
		messages.success(request,"Registered Successfully")
		return redirect('main')

# calling this below fn through js
@method_decorator(csrf_exempt,name='dispatch')
def check(request):
	n=request.POST.get('cname')
	try:
		RouterModel.objects.get(router_name=n)
		res = {"error":"Name is present already"}
	except RouterModel.DoesNotExist:
		res = {"msg":"Name is Available"}
	return JsonResponse(res)



def view_data(request):

	return render(request,'view.html',{'data':RouterModel.objects.all()})

def delete(request):
	id_no = request.GET.get('idn')

	RouterModel.objects.filter(idno=id_no).delete()
	return redirect('main')
def update(request):
	idn=request.GET.get('idn')
	res=RouterModel.objects.get(idno=idn)
	return render(request,'update.html',{'data':res})

def data_update(request):
	idn=request.POST.get('u1')
	n  =request.POST.get('u2')
	

	RouterModel.objects.filter(idno=idn).update(router_name=n)
	return redirect('main')
