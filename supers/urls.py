from django.urls import path
from . import views

urlpatterns = [
    path('', views.supers_list),
    path('<int:pk>/', views.supers_detail),
    path('<int:pk>/<str:power>/', views.supers_reassign),
]