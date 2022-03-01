from django.contrib import admin
from .models import Persona, Ciudad, TipoDocumento

# Register your models here.

admin.site.register(Persona)
admin.site.register(Ciudad)
admin.site.register(TipoDocumento)