from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^list/$', 'newsletter.views.list', name='list'),
    url(r'^search/$', 'newsletter.views.search', name='search'),
    url(r'^search_form/$', 'newsletter.views.search_view', name='search_view'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls))
] 

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
