from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length = 100, verbose_name = "Ismi")
    last_name = models.CharField(max_length = 100, verbose_name = "Familiyasi")
    date_of_birth = models.DateField(null = True, blank = True, verbose_name = "Tug`ilgan sana")
    date_of_death = models.DateField(null = True, blank = True, verbose_name = "Vafot etgan sana")
    biography = models.TextField(null = True, blank = True, verbose_name = "Biografiya")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"