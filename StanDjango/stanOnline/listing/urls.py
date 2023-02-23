from django.urls import path
from . import views

urlpatterns = [
    path('', views.listing_list, name="listing"),
    path('listing/<id>/', views.listing_retrieve, name="listing"),
    path("add_listing/", views.listing_create, name="listing"),
    path('listing/<pk>/edit/', views.listing_update, name="listing"),
    path('listing/<pk>/delete/', views.listing_delete, name="listing"),
]