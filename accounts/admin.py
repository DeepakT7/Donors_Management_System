from django.contrib import admin

# Register your models here.
from .models import Donor
from .models import Tag
from .models import Donation
from .models import Order

admin.site.register(Donor)
admin.site.register(Tag)
admin.site.register(Donation)
admin.site.register(Order)