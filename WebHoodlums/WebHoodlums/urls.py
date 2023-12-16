from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('team/', views.team, name="team"),
    path("login/",views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("form1/", views.form_view1, name="form1"),
    path("form2/",  views.form_view2, name="form2"),
    path("form3/",  views.form_view3, name="form3"),
    path("form4/",  views.form_view4, name="form4"),
    path('resume1/', views.resume_view1, name='resume_view1'),
    path('submit1/', views.submit_form1, name='submit_form1'),
    path('resume2/', views.resume_view2, name='resume_view2'),
    path('submit2/', views.submit_form2, name='submit_form2'),
    path('resume3/', views.resume_view3, name='resume_view3'),
    path('submit3/', views.submit_form3, name='submit_form3'),
    path('resume4/', views.resume_view4, name='resume_view4'),
    path('submit4/', views.submit_form4, name='submit_form4'),
]