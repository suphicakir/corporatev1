from django.contrib import admin
from . import models as m

# Register your models here.
@admin.register(m.Contact)
class AdminContact (admin.ModelAdmin):
    list_display=('full_name','email',)
