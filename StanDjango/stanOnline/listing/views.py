from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm
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

def listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() #this will create a new list
            return redirect("/")
    context = {
        "form": form
    }
    return render(request, "create.html", context)

def listing_update(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)
    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save() #this will create a new list
            return redirect("/")
    context = {
        "form": form
    }
    return render(request, "update.html", context)

def listing_delete(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect("/")