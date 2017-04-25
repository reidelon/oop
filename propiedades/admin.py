from django.contrib import admin

from .models import *

admin.site.register(String)
admin.site.register(Integer)


# admin.site.register(Enum)

class EnumAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')


admin.site.register(Enum, EnumAdmin)
