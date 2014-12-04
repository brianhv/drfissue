from django.conf.urls import patterns, include, url
from rest_framework import routers
from drftest.readonly import views
from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'drftest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    
)

