from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.generic import View
from e3.models import RouterModel
from django.contrib import messages
# from django.db.utils import IntegrityError
from rest_framework import viewsets
from .serializers import RouterSerializer

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
class RouterViewSet(viewsets.ModelViewSet):
    queryset = RouterModel.objects.all().order_by('name')
    serializer_class = RouterSerializer
class RouterDetails(View):
	def post(self,request):
		r_name	= request.POST.get('r1')
		ip_add	= request.POST.get('r2')
		r_type	= request.POST.get('r3')

		RouterModel(r_name=r_name,r_ip=ip_add,r_type=r_type).save()
		messages.success(request,"Saved Successfully")
		return redirect('main')

# calling this below fn through js
@method_decorator(csrf_exempt,name='dispatch')
def check(request):
	n=request.POST.get('cname')
	try:
		RouterModel.objects.get(name=n)
		res = {"error":"Name is present already"}
	except RouterModel.DoesNotExist:
		res = {"msg":"Name is Available"}
	return JsonResponse(res)


# -------------------------------------------------------------
def view_data(request):

	return render(request,'view.html',{'data':RouterModel.objects.all()})

def delete(request):
	id_no = request.GET.get('idn')

	RouterModel.objects.filter(r_ip=id_no).delete()
	return redirect('main')
def update(request):
	idn=request.GET.get('idn')
	res=RouterModel.objects.get(r_ip=idn)
	return render(request,'update.html',{'data':res})

def data_update(request):
	idn=request.POST.get('u1')
	n  =request.POST.get('u2')
	

	RouterModel.objects.filter(r_ip=idn).update(router_name=n)
	return redirect('main')

