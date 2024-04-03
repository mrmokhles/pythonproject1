"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app1 import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.SignupPage,name='signup'),

    path('login/',views.LoginPage,name='login'),

    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    
    path('saveEnquiry/',views.saveEnquiry,name='saveEnquiry'),

    path('contacts/',views.contactPage,name='contacts'),

    path('update/',views.UpdateBlog,name='update'),

    path('update/edit/<int:id>',views.EditBlog,name='edit'),

    path('up/<int:id>',views.up,name='up'),

    path('update/delete/<int:id>',views.deleteData,name='delete'),

    path('searchEmployee/',views.searchEmp,name='searchEmployee'),

    path('search/',views.searchBar,name='search'),

    path('countries_gdp_list', views.countries_gdp_list, name='countries_gdp_list'),
    path('countries_gdp_excel', views.countries_gdp_excel, name='countries_gdp_excel'),

    path('savecountries/',views.savecountries,name='savecountries'),

    path('import/',views.importExcel,name='import'),
    
]
