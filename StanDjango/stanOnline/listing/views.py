from django.shortcuts import render
from .models import Listing
# Create your views here.
#CRUD- create, retrieve, update, delete, list

def listing_list(request):
    listing= Listing.objects.all()
    context ={
        "listing": listing
    }
    return render(request, "listings.html", context)