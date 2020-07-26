"""Medicinecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from testapp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.display, name = 'home'),
    url(r'^contactus/', views.contact_us),
    url(r'^adminpage/', views.loginpage),
    url(r'^upload/', views.upload_view),
    url(r'^search/', views.Searchbar_view),
    url(r'^buy/', views.search),
    url(r'^show/', views.show),
    url(r'^profile/', views.profile_view),
    url(r'^input/', views.Buy_view),
    url(r'^termandpolicy/', views.term_view),
    url(r'^crud/', views.Buy1ListView.as_view(),name='crud'),
    url(r'^(?P<pk>\d+)/crud', views.Buy1DetailView.as_view(),name='detail'),
    url(r'^create/', views.Buy1CreateView.as_view()),
    url(r'^update/(?P<pk>\d+)/$', views.Buy1UpdateView.as_view()),
    url(r'^delete/(?P<pk>\d+)/$', views.Buy1DeleteView.as_view()),
    url(r'^signup/', views.signup_view),
    url(r'^logout123/', views.logout_view),
    url(r'^login/', views.loginpage),
    url('accounts/', include('django.contrib.auth.urls')),
]
