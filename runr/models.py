from django.db import models


class Rscript(models.Model):
    script = models.CharField(max_length=4000)
    df = models.CharField(max_length=200)

    def __str__(self):
        return self.script, self.df_name
