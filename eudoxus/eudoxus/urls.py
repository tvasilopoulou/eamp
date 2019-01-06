"""eudoxus URL Configuration

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
from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from apps import views as apps_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('?/', apps_views.construction, name='constr'),
    path('signup/', apps_views.signup, name='signup'),
    path('extraInfo/', apps_views.extraInfo, name='extraInfo'),
    path('profile/', apps_views.profile, name='profile'),
    path('', auth_views.LoginView.as_view(template_name="apps/home.html"), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name="apps/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="apps/home.html"), name='logout'),
    path('books/', apps_views.books, name='books'),
    path('students/dilosh', apps_views.dilosh, name='dilosh'),
    path('search/', apps_views.search, name='search'),

]
