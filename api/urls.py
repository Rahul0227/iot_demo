from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
# from .views import CreateView
# from .views import DetailsView
# from .views import UpdateView
# from .views import DeleteView
from rest_framework import routers
from .views import WeatherData
import requests
 

router = routers.DefaultRouter()
#router.register(r'bucketlist',DetailsView)

urlpatterns = {
#     url(r'^bucketlists/$', CreateView.as_view(), name="create"),
#     url(r'^bucketlists/(?P<pk>[0-9]+)/$',DetailsView.as_view(), name="details"),
#     url(r'^bucketlists/delete/(?P<pk>[0-9]+)/$',DeleteView.as_view(), name="Delete"),
#     url(r'^bucketlists/update/(?P<pk>[0-9]+)/$',UpdateView.as_view(), name="Update"),
#     #url('', include(router.urls)),
#     url('bucketlists/', include('rest_framework.urls', namespace='rest_framework'))
        url(r'^WeatherData/$',WeatherData.as_view(), name="list4")
}

urlpatterns = format_suffix_patterns(urlpatterns)





