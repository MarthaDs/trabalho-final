from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('candidate_list', views.candidate_list, name='candidate_list'),
    path('candidate/<int:pk>/', views.candidate_detail, name='candidate_detail'),
    path('candidate/new/', views.new_candidate, name='new_candidate'),
]