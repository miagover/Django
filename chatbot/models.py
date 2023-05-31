from django.db import models

# Create your models here.
class PastQ(models.Model):
    question = models.CharField(max_length=250)
    answer = models.TextField(max_length=4000)

    def __str__(self):
        return self.question