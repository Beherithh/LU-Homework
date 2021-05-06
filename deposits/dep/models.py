from django.db import models


class Deposit(models.Model):
    deposit = models.BigIntegerField()
    term = models.IntegerField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    def interest(self):
        temp = self.deposit
        for i in range(self.term):
            temp *= (1 + self.rate)
        temp -= self.deposit
        return temp
