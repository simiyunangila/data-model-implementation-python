from django.contrib import admin
from.models import Criminal

# Register your models here.

class CriminalAdmin(admin.ModelAdmin):
    list_display = ('judge_name','lawyer_name','date_created','date_updated','stock','description','price')

admin.site.register(Criminal,CriminalAdmin)


