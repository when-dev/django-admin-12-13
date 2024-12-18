from django.shortcuts import render, redirect
from .models import Ownership
from .forms import VehicleForm, OwnerForm, OwnershipForm

def vehicle_list(request):
    ownerships = Ownership.objects.all()
    return render(request, 'transport_app/vehicle_list.html', {'ownerships': ownerships})

def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'transport_app/add_vehicle.html', {'form': form})

def add_owner(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = OwnerForm()
    return render(request, 'transport_app/add_owner.html', {'form': form})

def add_ownership(request):
    if request.method == 'POST':
        form = OwnershipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = OwnershipForm()
    return render(request, 'transport_app/add_ownership.html', {'form': form})
