from django.contrib import admin

from .models import Igreja, Culto




class CultoAdmin(admin.ModelAdmin):
    list_display = ("nome_do_culto","data","igreja")




admin.site.register(Igreja)
admin.site.register(Culto,CultoAdmin)








# Register your models here.
