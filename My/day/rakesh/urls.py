from django.urls import path
from . import views
urlpatterns = [
	path('',views.home),
	path('hh/',views.homepage,name="homepage"),
	path('lg/',views.lgn,name="lgn"),
	path('rg/',views.reg,name="reg"),
	path('re/',views.ree,name="ree"),
]