from django.urls import path
from . import views

urlpatterns = [
    path('', views.supers_list),
    path('<int:pk>/', views.supers_detail),
    path('<int:pk>/<int:power>/', views.supers_reassign), #int:pk gives primary key of super, int:power gives primary key of power to give to super
]