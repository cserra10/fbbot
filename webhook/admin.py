from .models import Denuncia, File
from django.contrib import admin


class DenunciaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Denuncia, DenunciaAdmin)
