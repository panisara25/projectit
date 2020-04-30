from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('company_profile', views.companyProfile, name='company_profile'),
    path('company_profile/<int:id>',views.editcompany, name='editcompany'),
    path('profile', views.profile, name='profile'),
    path('profile/<int:id>',views.editprofile, name='edit')
]

