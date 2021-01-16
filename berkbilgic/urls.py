"""onurbilgic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.contrib.auth.views import LoginView,LogoutView

from core.views import HomePageDetailView, AboutPageDetailView
from berkbilgic import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^$", HomePageDetailView.as_view(), name="home"),
    url(r'^about/$',AboutPageDetailView.as_view(),name='about'),
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('core/', include(('core.urls', 'core'), namespace='core')),
    path('language/', include(('language.urls', 'core'), namespace='language')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
