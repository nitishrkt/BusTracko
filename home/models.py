from django.db import models
# Create your models here.
class Wallet(models.Model):
    wallet_id = models.AutoField(primary_key=True )
    username = models.CharField(max_length=50, unique=True)
    balance = models.IntegerField()

    def __str__(self):
        return self.username