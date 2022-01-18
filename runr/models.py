from django.db import models


class Rscript(models.Model):
    Rscript_code = models.CharField(max_length=4000)

    def __str__(self):
        return self.Rscript_code



