from django.db import models
from django.contrib import admin
class Bank(models.Model):
      Name=models.CharField(max_length=10)
      Accountno=models.IntegerField(primary_key="Accountno")
      Aadharno=models.IntegerField()
      DoB=models.DateField()
      Branch=models.CharField(max_length=21)
class BankAdmin(admin.ModelAdmin):
      list_display=('Name','Accountno','Aadharno','DoB','Branch')

