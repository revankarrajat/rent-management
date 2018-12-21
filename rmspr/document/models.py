from django.db import models

# Create your models here.

class document(models.Model):
    doc_id = models.PositiveIntegerField(primary_key=True)
    doc = models.TextField()
    doc_content_type = models.CharField(max_length=100)
    description = models.TextField()
    #tenantid = models.ForeignKey('tenant.tenant',related_name='tenantid+',null=True,blank=True)
