"""imageenhance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from imageapp import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.login),
    path('registration/',views.registration),
      path('userviewgalary/',views.userviewgalary),
      path('userhome/',views.userhome),
       path('useraddimage/',views.useraddimage),
       path('imageenhances/',views.imageenhances),
         path('feedback/',views.feedback),
  path('adminviewfeedback/',views.adminviewfeedback),
    path('adminviewusers/',views.adminviewusers),
      path('resizeimage/',views.resizeimage),
     path('changeformat/',views.changeformat),
     path('resize/',views.resize),


 
]
