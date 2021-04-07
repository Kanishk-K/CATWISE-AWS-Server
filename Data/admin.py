from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .resources import CatWiseResource
from.models import CatWise
# Register your models here.
class CatWiseAdmin(ImportExportModelAdmin):
    resource_class = CatWiseResource
    pass
admin.site.register(CatWise, CatWiseAdmin)