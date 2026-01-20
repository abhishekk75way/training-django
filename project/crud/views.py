from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import SignUpForm

# Create your views here.
def home(request):
    return HttpResponse("Hello from Crud Operations!")

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("item_list")
    else:
        form = SignUpForm()

    return render(request, "registration/signup.html", {"form": form})

@login_required
def item_list(request):
    items = Item.objects.filter(user=request.user)
    return render(request, "list.html", {"items": items})

@login_required
def item_create(request):
    if request.method == "POST":
        Item.objects.create(
            user=request.user,
            name=request.POST.get("name"),
            description=request.POST.get("description"),
            price=request.POST.get("price"),
        )
        return redirect("item_list")
    return render(request, "create.html")

@login_required
def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        item.name = request.POST.get("name")
        item.description = request.POST.get("description")
        item.price = request.POST.get("price")
        item.save()
        return redirect("item_list")
    return render(request, "update.html", {"item": item})

@login_required
def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == "POST":
        item.delete()
        return redirect("item_list")

    return render(request, "delete.html", {"item": item})