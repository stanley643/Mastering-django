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

def listing_retrieve(request, id):
    listing = Listing.objects.get(id=id)
    context = {
        "listing": listing
    }
    return render(request, "listing.html", context)