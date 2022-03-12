from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.generic.base import RedirectView, TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('home.urls')),
    url(r'^(?!/?static/)(?P<path>.*\..*)$',
        RedirectView.as_view(url='/static/%(path)s', permanent=False)),
]