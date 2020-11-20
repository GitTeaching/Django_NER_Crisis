from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('get_wwww_event/', views.get_wwww_event, name='get_wwww_event'),
]