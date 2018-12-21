from django.contrib import admin

# Register your models here.
from.models import leasess,renewal

class leaseadmin(admin.ModelAdmin):
    pass
class renewaladmin(admin.ModelAdmin):
    pass
admin.site.register(leasess,leaseadmin)
admin.site.register(renewal,renewaladmin)