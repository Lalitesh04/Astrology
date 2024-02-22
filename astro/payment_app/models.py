from django.db import models


class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    orderid = models.CharField(max_length=20)

    class Meta:
        db_table = "payment_table"

    def __str__(self):
        return self.name
