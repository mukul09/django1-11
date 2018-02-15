from django.contrib import admin
from .models import RestaurantLocation
# Register your models here.




class RestaurantLocationAdmin(admin.ModelAdmin):
	list_display=('name','location','category')
	search_fields=('name','category')			# the search could be done on these fields
	date_hierarchy='timestamp'					# the show the years when object was made
	#fields=('name',)							#fields should be tuple or list, is used to allow make changes by the user 
	#filter_horizontal=('name',)                #only applicable for ManyToMany fields

admin.site.register(RestaurantLocation,RestaurantLocationAdmin)