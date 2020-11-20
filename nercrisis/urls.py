from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('home/', views.home, name='home'),
	path('extract_event/', views.extract_event, name='extract_event'),
	path('extract_event_using_api/', views.extract_event_using_api, name='extract_event_using_api'),
	path('extract_events_from_twitter/', views.extract_events_from_twitter, name='extract_events_from_twitter'),
	path('profile/', views.profile, name='profile'),
	path('add_report/', views.add_report, name='add_report'),
	path('update_report/<str:id>', views.update_report, name='update_report'),
	path('delete_report/<str:id>', views.delete_report, name='delete_report'),
]