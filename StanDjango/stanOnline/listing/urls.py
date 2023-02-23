from django.urls import path
from . import views

urlpatterns = [
    path('', views.listing_list, name="listing"),
    path('listing/<id>/', views.listing_retrieve, name="listing"),
    path("add_listing/", views.listing_create, name="listing"),
]