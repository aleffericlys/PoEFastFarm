from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('users', views.get_users, name='get_all_users'),
	path('essences/<str:nick>', views.get_user_escences, name='get_user_essences'),
	# path('essences/delete/<str:id>', views.delete_essence, name='delete_essence'),
	path('oils/<str:nick>', views.get_user_oils, name='get_user_oils'),
	# path('oils/delete/<str:id>', views.delete_oil, name='delete_oil'),
	path('scarabs/<str:nick>', views.get_user_scarabs, name='get_user_scarabs'),
	# path('scarabs/delete/<str:id>', views.delete_scarab, name='delete_scarab'),
	path('user/<str:nick>', views.get_users_by_nick, name='get_user_by_nick'),
	path('data/', views.user_manager),



	path('teste', views.teste, name='teste')
]
