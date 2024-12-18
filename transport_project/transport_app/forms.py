from django import forms
from .models import Vehicle, Owner, Ownership

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['model', 'year']

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['name', 'contact']

class OwnershipForm(forms.ModelForm):
    class Meta:
        model = Ownership
        fields = ['vehicle', 'owner']