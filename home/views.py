from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class home(View):
	def get(self,request):
		template_name = 'home/index.html'
		return render(request,template_name)
