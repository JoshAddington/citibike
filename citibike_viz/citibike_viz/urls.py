from django.conf.urls import include, url
from django.contrib import admin
from . import views
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'citibike_viz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
    url(r'^$', 'citibike_viz.views.home', name='home'),
]
