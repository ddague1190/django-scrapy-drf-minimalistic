from django.db import models



class Manufacturer(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name

class Bike(models.Model):
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    mfg = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model = models.CharField(max_length=200)

    def __str__(self) -> str:
        tmp = '-' + str(self.end_year) if (self.start_year != self.end_year) else ''
        return f"{self.start_year}{tmp} {self.model}"

    @property
    def year(self):
        return 'dummy_val'