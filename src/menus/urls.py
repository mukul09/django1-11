
from django.conf.urls import url



from .views import (
    ItemListView,
    ItemDetailView,
    ItemCreateView,
    ItemUpdateView,
    )


urlpatterns = [
   
    url(r'^$', ItemListView.as_view(), name='list'),
    url(r'^create/$',ItemCreateView.as_view(), name ='create'), #class based view
    #url(r'^(?P<pk>\d+)/edit/$', ItemUpdateView.as_view(), name="edit"),
    url(r'^(?P<pk>\d+)/$', ItemUpdateView.as_view(), name="detail"),
    
]


