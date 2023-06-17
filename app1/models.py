# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Switches(models.Model):
    sw = models.CharField(max_length=255, blank=True, null=True)
    t1 = models.IntegerField(blank=True, null=True)
    t2 = models.IntegerField(blank=True, null=True)
    t3 = models.IntegerField(blank=True, null=True)
    t4 = models.IntegerField(blank=True, null=True)
    t5 = models.IntegerField(blank=True, null=True)
    ts = models.CharField(max_length=255, blank=True, null=True)
    ts2 = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'switches'
        
    # def __str__(self):
    #     return self.sw
