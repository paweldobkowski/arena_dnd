from django.db import models


class TabelaTestowa(models.Model):
    pierwsze_dane = models.TextField()
    i_inne_dane = models.BooleanField()
