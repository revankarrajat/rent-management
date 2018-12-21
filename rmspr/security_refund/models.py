from django.db import models

# Create your models here.
class securiyt_refund(models.Model):
    id = models.AutoField(primary_key=True)
    refund_amount = models.PositiveIntegerField()
    date = models.DateField()
    refund_reason = models.TextField()
    termination_id = models.ForeignKey('termination.termination',related_name='terminationid+',null=True,blank=True,on_delete=models.CASCADE)
    employee_id = models.ForeignKey('employee.employee',related_name='employee_id+',null=True,on_delete= models.CASCADE,blank=True)