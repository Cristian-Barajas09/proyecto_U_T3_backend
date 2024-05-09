from django.db import models

class Currency(models.Model):
    title = models.CharField(max_length=250)
    code = models.CharField(max_length=5)

class CurrencyConverter(models.Model):
    from_currency = models.ForeignKey(Currency, related_name='from_currency', on_delete=models.CASCADE)
    to_currency = models.ForeignKey(Currency, related_name='to_currency', on_delete=models.CASCADE)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=4)
    
    def __str__(self):
        return f'{self.from_currency.code} to {self.to_currency.code}'