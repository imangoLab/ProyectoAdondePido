from django.contrib import admin
from .models import Presentacion

class PresentacionAdmin(admin.ModelAdmin):
	list_display = ("capacidad", )

admin.site.register(Presentacion, PresentacionAdmin)

#default
from .models import Producto
admin.site.register(Producto)