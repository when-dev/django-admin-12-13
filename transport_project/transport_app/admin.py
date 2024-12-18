from django.contrib import admin
from .models import Vehicle, Owner, Ownership

admin.site.register(Vehicle)
admin.site.register(Owner)
admin.site.register(Ownership)
