"""emailapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns as fs
from emailapps import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('mails/', views.Maills.as_view()), # inbox+ outbox+draft
    url('send_email', views.send_email),# to conform its sent
    url(r'^$', views.home),
    url('inboxs/', views.Inbox.as_view()),# user specific inbox API responses
    url('outboxs/', views.Outboxs.as_view()),# user specific outbox API responses
    url('trash/', views.Trash.as_view()),
    url('drafts/', views.Draftss.as_view()),

]
urlpatterns=fs(urlpatterns)