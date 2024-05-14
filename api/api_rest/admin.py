from django.contrib import admin

from .models import User, Essences, Oils, Scarabs
# Register your models here.
admin.site.register(User)
admin.site.register(Essences)
admin.site.register(Oils)
admin.site.register(Scarabs)