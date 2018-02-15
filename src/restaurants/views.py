 
# Create your views here.

# def home(request):
# 	html_temp='Mukul Agrawal'
# 	html_="""
# 	<html lang=en>
# 	<head>
# 	</head>
# 	<body>
# 	<h1> My name is {html_temp}</h1>.format(html_temp=html_temp)
# 	<p> I am a  student</p>
# 	</body>
# 	</html>
# 	"""
# return HttpResponse(html_)



from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView,CreateView, UpdateView
from django.db.models import Q
# Create your views here.

# class HomeView(TemplateView):
#     template_name = 'home.html'

#     def get_context_data(self, *args, **kwargs):
#         context = super(HomeView, self).get_context_data(*args, **kwargs)
#         num = None
#         some_list = [
#             random.randint(0, 100000000), 
#             random.randint(0, 100000000), 
#             random.randint(0, 100000000)
#         ]
#         condition_bool_item = True
#         if condition_bool_item:
#             num = ranodm.randint(0, 100000000)
#         context = {
#             "num": num, 
#             "some_list": some_list
#         }
#         # points=[{"1","2"},{2,3},{3,4}]
#         # context={
#         # "points":points
#         # }



#         return context



from .models import RestaurantLocation
from .forms import RestaurantCreateForm,RestaurantLocationCreateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def restaurants_listview(request,):
    template_name = 'restaurants/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)


# class RestaurantListView(ListView):
# 	template_name='restaurants/restaurants_list.html'
# 	def get_queryset(self):
# 		slug=self.kwargs.get("slug")
# 		if slug:
# 			queryset=RestaurantLocation.objects.filter(
# 				Q(category__iexact=slug)|
# 				Q(category__icontains=slug)
# 				)
# 		else:
# 			queryset=RestaurantLocation.objects.all()
# 		return queryset 


class RestaurantListView(LoginRequiredMixin, ListView):
	#template_name='restaurants/restaurants_list.html'
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)



class RestaurantDetailView(LoginRequiredMixin, DetailView):
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)

	# def get_context_data(self,*args,**kwargs):
	# 	context=super(RestaurantDetailView, self).get_context_data(*args,**kwargs)
	# 	return context
	
	# def get_object(self,*args,**kwargs):
	# 	rest_id=self.kwargs.get("rest_id")
	# 	obj=get_object_or_404(RestaurantLocation, id=rest_id) #pk=rest_id
	# 	return obj


class RestaurantCreateView(LoginRequiredMixin, CreateView):					# alternative of the restuarant_createview
	form_class=RestaurantLocationCreateForm
	login_url='/login/'
	template_name='form.html'
	#success_url='/restaurants/'

	def form_valid(self, form):
		instance=form.save(commit=False)
		instance.owner=self.request.user
		return super(RestaurantCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context=super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
		context['title']= 'Add Restaurant'
		return context


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):					# alternative of the restuarant_createview
	form_class=RestaurantLocationCreateForm
	login_url='/login/'
	template_name='restaurants/detail-update.html'
	#success_url='/restaurants/'


	def get_context_data(self, *args, **kwargs):
		context=super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
		context['title']= 'Update Restaurant'
		return context

	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)





# def search_form(request):
# 	return render(request,'search_form.html')

# def search(request):
# 	if 'q' in request.GET and request.GET['q']:
# 		q=request.GET['q']
# 		queryset=RestaurantLocation.objects.filter(name__icontains=q)
# 		print(queryset)
# 		return render(request,'search_result.html',{'queryset':queryset})
# 		# message='you searched for %r' % request.GET['q']
# 	else:
# 		message='you submitted an empty search'
# 		return HttpResponse(message)

