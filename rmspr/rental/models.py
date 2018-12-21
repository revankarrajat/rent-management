from django.db import models

# Create your models here.
class rent(models.Model):
    id = models.AutoField(primary_key=True)
    rent_amt = models.DecimalField(max_digits=10,decimal_places=2)
    rent_paid_date = models.DateField()
    date_to_pay = models.DateField()
    paid_amt = models.DecimalField(max_digits=10,decimal_places=2)
    maintenance_amt = models.DecimalField(max_digits=10,decimal_places=2)
    tax_amt = models.DecimalField(max_digits=10,decimal_places=2)
    bal_amt = models.DecimalField(max_digits=10,decimal_places=2)
    tenant_id = models.ForeignKey('tenant.tenant',related_name='id+',null=True,on_delete= models.CASCADE,blank=True)
    lease_id = models.ForeignKey('leasess.leasess',related_name='leasessid+',null=True,blank=True,on_delete=models.CASCADE)
    payment_id = models.ForeignKey('trancations.trancations',related_name='id+',null=True,on_delete=models.CASCADE)
