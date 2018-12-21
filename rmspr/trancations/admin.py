from django.contrib import admin

# Register your models here.
from.models import trancations,checkpayment,creditcard

class trancationsadmin(admin.ModelAdmin):
    pass
class checkpaymentadmin(admin.ModelAdmin):
    pass
class creditcardadmin(admin.ModelAdmin):
    pass

admin.site.register(trancations, trancationsadmin)
admin.site.register(checkpayment,checkpaymentadmin)
admin.site.register(creditcard,creditcardadmin)

