from django.contrib import admin
from .models import Model,Make,BodyType,Car,Image


class CarAdmin(admin.ModelAdmin):
    list_display=('model','year','make','body','isAvailable','isFeatured','locationValue','mileage','engineSize','drive','transmission','horsePower','acceleration','fuelType')

admin.site.register(Model)
admin.site.register(Make)
admin.site.register(BodyType)
admin.site.register(Car)
admin.site.register(Image)