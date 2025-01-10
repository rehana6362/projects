from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL -> home view
    path('candidate/<int:candidate_id>/', views.candidate_list, name='candidate_list'),
]
