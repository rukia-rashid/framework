from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Street)
admin.site.register(NormalUser)
admin.site.register(HealthFacility)
admin.site.register(Patient)
admin.site.register(Deceased)
admin.site.register(Recovered)