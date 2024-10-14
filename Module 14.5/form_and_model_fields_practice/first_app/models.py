from django.db import models

# Create your models here.
class ModelForm(models.Model):
    # auto_field = models.AutoField(primary_key=True)
    # big_auto_field = models.BigAutoField(primary_key=True)
    # big_integer_field = models.BigIntegerField()
    # boolean_field = models.BooleanField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date_time = models.DateField()
    decimal_field = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name
