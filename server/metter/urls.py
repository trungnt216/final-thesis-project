from django.conf.urls import url 
from metter import views 
 
urlpatterns = [ 
    url(r'^api/metters$', views.metter_list),
    url(r'^api/metters/(?P<pk>[0-9]+)$', views.metter_detail),
    url(r'^api/metter/latest', views.get_latest_metter_from_3phase),
    url(r'^api/metter/graph', views.get_metter_graph)
    #url(r'^api/metters/published$', views.tutorial_list_published)
]