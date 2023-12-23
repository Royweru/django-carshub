from django.contrib import admin
from .models import Model,Make,BodyType

admin.site.register(Model)
admin.site.register(Make)
admin.site.register(BodyType)