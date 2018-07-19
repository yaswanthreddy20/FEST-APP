from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dosar.views.home', name='home'),
    # url(r'^dosar/', include('dosar.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^spot/$', 'web.views.spot_reg', name='vote'),
    url(r'^special/$','web.views.special_nights'),
    
    url(r'^$','web.views.index'),
	url(r'^sponsors/$','web.views.sponsors'),
	url(r'^visitors/$','web.views.visitors'),
	url(r'^registration/$','web.views.spot_reg'),
	url(r'^vehicle/$','web.views.vehicle_pass'),
	url(r'^vehiclepass/$','web.views.vehicle'),
    url(r'^details/(?P<model>\w+)/(?P<search>\w+)/$','web.views.details'),
    url(r'^searchquerie/$','web.views.searchquerie'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^login/$','web.views.login'),
)
urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATICFILES_DIRS}),
    )
