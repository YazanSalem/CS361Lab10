"""CS361Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from TAScheduler.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view()),
    path('home/', Home.as_view()),
    path('createuser/', CreateUser.as_view()),
    path('createcourse/', CreateCourse.as_view()),
    path('createlab/', CreateLab.as_view()),
    path('accountsettings/', AccountSettings.as_view()),
    path('edituser/', EditUser.as_view()),
    path('editcourse/', EditCourse.as_view()),
    path('editlab', EditLab.as_view()),
]
