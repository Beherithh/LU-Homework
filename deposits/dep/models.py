from django.db import models


class Deposit(models.Model):
    deposit = models.BigIntegerField()
    term = models.IntegerField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    interest = models.DecimalField(max_digits=10000, decimal_places=2)

    def interest(self):
        temp = self.deposit
        for i in range(self.term):
            temp *= self.rate
        self.interest -= self.deposit
        return self.interest
