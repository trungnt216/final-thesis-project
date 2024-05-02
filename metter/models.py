from django.db import models

# Create your models here.
# models.py

from django.db import models

class Metter(models.Model):
    id = models.AutoField(primary_key=True)
    airms = models.DecimalField(max_digits=10, decimal_places=2)
    birms = models.DecimalField(max_digits=10, decimal_places=2)
    cirms = models.DecimalField(max_digits=10, decimal_places=2)
    avrms = models.DecimalField(max_digits=10, decimal_places=2)
    bvrms = models.DecimalField(max_digits=10, decimal_places=2)
    cvrms = models.DecimalField(max_digits=10, decimal_places=2)
    awatt = models.DecimalField(max_digits=10, decimal_places=2)
    bwatt = models.DecimalField(max_digits=10, decimal_places=2)
    cwatt = models.DecimalField(max_digits=10, decimal_places=2)
    avar = models.DecimalField(max_digits=10, decimal_places=2)
    bvar = models.DecimalField(max_digits=10, decimal_places=2)
    cvar = models.DecimalField(max_digits=10, decimal_places=2)
    ava = models.DecimalField(max_digits=10, decimal_places=2)
    bva = models.DecimalField(max_digits=10, decimal_places=2)
    cva = models.DecimalField(max_digits=10, decimal_places=2)
    awatthr_hi = models.DecimalField(max_digits=10, decimal_places=2)
    bwatthr_hi = models.DecimalField(max_digits=10, decimal_places=2)
    cwatthr_hi = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.BigIntegerField()
    index = models.IntegerField()
    
    class Meta:
        db_table = 'metter'  # Specify the name of the table in the PostgreSQL database
