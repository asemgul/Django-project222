from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Flightofusers)


# Register your models here.
admin.site.register(City)
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Day)

