from django.db import models

class Test(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        db_table = 'tests'